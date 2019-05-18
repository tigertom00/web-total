from django.shortcuts import redirect, reverse, get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Sum
from timelister.forms import TimelisteForm
from matriell.forms import MatriellForm
from .forms import JobberForm, EditJobbForm, JobbImageForm
from . import models
from matriell import models as m_models
from timelister import models as t_models
from datetime import datetime, timedelta

User = get_user_model()
today = datetime.now()
firstday = today.replace(day=1)
redirect_if_referer_not_found = '/'


# Jobb List View
# TODO: look at pagination
@login_required
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
    return render(request, 'jobb/jobblist.html', context)


# Jobb Detail View
@login_required
def jobbdetail(request, jobb_id):
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    bilder = models.JobbImage.objects.filter(jobb=jobb)
    matriell = m_models.Matriell.objects.all()
    timer = t_models.Timeliste.objects.filter(jobb__pk=jobb_id)
    total_timer_jobb = timer.aggregate(Sum('timer'))
    if request.method == "POST":
        bilderform = JobbImageForm(request.POST,
                                   request.FILES, initial={'jobb': jobb})
        if bilderform.is_valid():
            bilderform.save()
            messages.success(request, 'Bilder Lagt til')
            return redirect(reverse("jobbdetail", kwargs={
                'jobb_id': jobb_id
            }))
    bilderform = JobbImageForm(initial={'jobb': jobb})
    context = {
        'bilderform': bilderform,
        'bilder': bilder,
        'total_timer_jobb': total_timer_jobb,
        'timer': timer,
        'jobb': jobb,
        'matriell': matriell,
    }
    return render(request, 'jobb/jobbdetail.html', context)


# Edit jobb Form
@login_required
def editjobb(request, jobb_id):
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    if request.method == "POST":
        editjobb = EditJobbForm(request.POST,
                                request.FILES, instance=jobb)
        if editjobb.is_valid():
            editjobb.save()
            messages.success(request, 'Jobb oppdatert')
            return redirect(reverse("jobbdetail", kwargs={
                'jobb_id': jobb_id
            }))
    editjobb = EditJobbForm(instance=jobb)
    context = {
        'editjobb': editjobb,
    }
    return render(request, 'jobb/editjobb.html', context)


# Delete Jobber
@login_required
def jobberDelete(request, jobb_id):
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    jobb.delete()
    messages.warning(request, 'Jobb deleted.')
    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))


# Add Matriell To Jobber
@login_required
def jobbMatriell(request, jobb_id):
    jobb = get_object_or_404(models.Jobber, pk=jobb_id)
    matriell = m_models.Matriell.objects.all()
    context = {
        'matriell': matriell,
        'jobb': jobb,
    }
    return render(request, 'jobb/jobb_matriell.html', context)
