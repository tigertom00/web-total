from django.shortcuts import redirect, reverse, get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Sum, Count
from timelister.forms import TimelisteForm, JobberForm, EditJobbForm, MatriellForm, ModalTimerForm
from timelister import models
from datetime import datetime, timedelta
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy

User = get_user_model()
today = datetime.now()
firstday = today.replace(day=1)
redirect_if_referer_not_found = '/'

# Not in use


def new_timeliste(request):

    timeform = TimelisteForm(request.POST or None)
    if request.method == "POST":
        if timeform.is_valid():
            timeform.instance.user = request.user
            timeform.save()
            return redirect(reverse("new_timeliste"))
    context = {
        'timeform': timeform,

    }

    return render(request, 'timelister/new_timeliste.html', context)

# NOT IN USE


def new_jobb(request):

    jobb_list = models.Jobber.objects.all()
    most_recent = models.Jobber.objects.order_by('-timestamp')[:3]
    paginator = Paginator(jobb_list, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    jobbform = JobberForm(request.POST or None)

    if request.method == "POST":
        if jobbform.is_valid():
            jobbform.save()
            messages.success(request, 'Jobb Lagt til')
            return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))
    context = {
        'jobbform': jobbform,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
    }

    pass

# Timelister #

# Timeliste Current month List View


def timeliste(request):
    current_month = datetime.now().month
    this_month_timer = models.Timeliste.objects.filter(
        dato__month=current_month).filter(user=request.user).order_by('dato')
    total_timer = this_month_timer.aggregate(Sum('timer'))
    timeform = TimelisteForm(request.POST or None)
    print(this_month_timer)
    if request.method == "POST":
        if timeform.is_valid():
            timeform.instance.user = request.user
            timeform.save()
            messages.success(request, 'Timer Lagt til')
            return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))

    context = {
        'timeform': timeform,
        'total_timer': total_timer,
        'this_month_timer': this_month_timer,
    }
    return render(request, 'timelister/timeliste.html', context)

# Timeliste Last Month List View


def timelisteLastmonth(request):
    last_month = datetime.now().month-1
    lastMonth = firstday - timedelta(days=1)
    last_month_timer = models.Timeliste.objects.filter(
        dato__month=last_month).filter(user=request.user).order_by('dato')
    total_timer_lastmonth = last_month_timer.aggregate(Sum('timer'))
    timeform = TimelisteForm(request.POST or None)
    if request.method == "POST":
        if timeform.is_valid():
            timeform.instance.user = request.user
            timeform.save()
            messages.success(request, 'Timer Lagt til')
            return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))
    context = {
        'timeform': timeform,
        'last_month_timer': last_month_timer,
        'total_timer_lastmonth': total_timer_lastmonth,
        'lastMonth': lastMonth,
    }

    return render(request, 'timelister/timeliste_lastmonth.html', context)

# Delete Timer


def timerDelete(request, object_id):
    object = get_object_or_404(models.Timeliste, pk=object_id)
    object.delete()
    messages.warning(request, 'Timer deleted.')
    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))

# Jobber #

# Jobb List View


def jobblist(request):
    jobb_list = models.Jobber.objects.all()
    most_recent = models.Jobber.objects.order_by('-date')
    paginator = Paginator(jobb_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    jobbform = JobberForm(request.POST or None)
    if request.method == "POST":
        if jobbform.is_valid():
            jobbform.save()
            messages.success(request, 'Jobb Lagt til')
            return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))
    context = {
        'jobbform': jobbform,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
    }
    return render(request, 'timelister/jobblist.html', context)


# Jobb Detail View

def jobbdetail(request, jobb_id):
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    matriell = models.Matriell.objects.all()
    timer = models.Timeliste.objects.filter(jobb__pk=jobb_id)
    total_timer_jobb = timer.aggregate(Sum('timer'))
    editjobb = EditJobbForm(request.POST or None, instance=jobb)
    jobbform = JobberForm(request.POST or None)
    if request.method == "POST":
        if jobbform.is_valid():
            jobbform.save()
            messages.success(request, 'Jobb Lagt til')
            return redirect(reverse("jobbdetail", kwargs={
                'jobb_id': jobbform.instance.ordre_nr
            }))
        elif editjobb.is_valid():
            editjobb.save()
            messages.success(request, 'Jobb oppdatert')
            return redirect(reverse("jobbdetail", kwargs={
                'jobb_id': editjobb.instance.ordre_nr
            }))
    context = {
        'total_timer_jobb': total_timer_jobb,
        'timer': timer,
        'jobb': jobb,
        'jobbform': jobbform,
        'editjobb': editjobb,
        'matriell': matriell,
    }
    return render(request, 'timelister/jobbdetail.html', context)

# Delete Jobber


def jobberDelete(request, object_id):
    object = get_object_or_404(models.Jobber, pk=object_id)
    object.delete()
    messages.warning(request, 'Jobb deleted.')
    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))

# Add Matriell To Jobber


def jobbMatriell(request, jobb_id):
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    matriell = models.Matriell.objects.all()
    context = {
        'matriell': matriell,
        'jobb': jobb,
    }
    return render(request, 'timelister/jobb_matriell.html', context)

# Matriell #

# Matriell List View


def matriellList(request):
    matriell = models.Matriell.objects.all()
    matriellform = MatriellForm(request.POST or None)
    if request.method == "POST":
        if matriellform.is_valid():
            matriellform.save()
            messages.success(request, 'Matriell Lagt til')
            return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))
    context = {
        'matriell': matriell,
        'matriellform': matriellform
    }
    return render(request, 'timelister/matiell-liste.html', context)

# Matriell Detail View


def matriellDetail(request, object_id):
    matriell = get_object_or_404(models.Matriell, pk=object_id)
    context = {
        'matriell': matriell,
    }
    return render(request, 'timelister/matriell-detail.html', context)

# Delete Matriell


def matriellDelete(request, object_id):
    object = get_object_or_404(models.Matriell, pk=object_id)
    object.delete()
    messages.warning(request, 'Matriell deleted.')
    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))


# Add Matriell to jobb

def add_matriell(request, object_id, jobb_id, antall):
    matriell = get_object_or_404(models.Matriell, pk=object_id)
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    jobb_matriell, created = models.JobbMatriell.objects.get_or_create(
        matriell=matriell,
        jobb=jobb,
        transf=False)

    if jobb.matriell.filter(matriell__pk=matriell.pk).exists():
        if created:
            jobb.matriell.add(jobb_matriell)
            jobb_matriell.antall += int(antall)-1
            jobb_matriell.save()
            messages.success(request, 'Matriell Lagt til')
        else:
            jobb_matriell.antall += int(antall)
            jobb_matriell.save()
            messages.success(request, 'Matriell oppdatert')
    else:
        jobb.matriell.add(jobb_matriell)
        jobb_matriell.antall += int(antall)-1
        jobb_matriell.save()
        messages.success(request, 'Matriell Lagt til')

    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))

# Delete Matriell from Jobb


def delete_matriell(request, object_id, jobb_id, antall):
    matriell = get_object_or_404(models.Matriell, pk=object_id)
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    jobb_matriell = models.JobbMatriell.objects.get(
        matriell=matriell,
        jobb=jobb,
        transf=False)

    if jobb.matriell.filter(matriell__pk=matriell.pk).exists():
        if jobb_matriell.antall >= 2:
            jobb_matriell.antall += int(antall)
            jobb_matriell.save()
            if jobb_matriell.antall <= 0:
                jobb.matriell.remove(jobb_matriell)
                jobb_matriell.delete()
        else:
            jobb.matriell.remove(jobb_matriell)
            jobb_matriell.delete()
        messages.warning(request, 'Matriell deleted.')

    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))

# Set Matriell to transfered on jobb


def transf_matriell(request, object_id, jobb_id, transf):
    matriell = get_object_or_404(models.Matriell, pk=object_id)
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    jobb_matriell = models.JobbMatriell.objects.get(
        matriell=matriell,
        jobb=jobb,
        transf=False)

    if jobb.matriell.filter(matriell__pk=matriell.pk).exists():
        if transf == '50':
            if jobb_matriell.transf:
                messages.warning(request, 'Alerede Overført.')
            else:
                jobb_matriell.transf = True
                jobb_matriell.save()
                messages.info(request, 'Matriell Overført.')

    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))

# Modal Timer Form, from django-bootstrap-modal-forms==1.4.2


class ModalTimerView(BSModalCreateView):
    template_name = 'func/modal_timer_form.html'
    form_class = ModalTimerForm
    success_message = 'Timer lagt til.'
    success_url = reverse_lazy('timeliste')
