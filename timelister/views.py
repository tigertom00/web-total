from django.shortcuts import redirect, reverse, get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Sum, Count
from timelister.forms import TimelisteForm, ModalTimerForm
from jobb.forms import JobberForm, EditJobbForm
from matriell.forms import MatriellForm
from timelister import models
from matriell import models as m_models
from jobb import models as j_models
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

    jobb_list = j_models.Jobber.objects.all()
    most_recent = j_models.Jobber.objects.order_by('-timestamp')[:3]
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


# Modal Timer Form, from django-bootstrap-modal-forms==1.4.2


class ModalTimerView(BSModalCreateView):
    template_name = 'func/modal_timer_form.html'
    form_class = ModalTimerForm
    success_message = 'Timer lagt til.'
    success_url = reverse_lazy('timeliste')
