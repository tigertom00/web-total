from django.shortcuts import render
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Sum
from timelister.forms import TimelisteForm, JobberForm, MatriellForm
from timelister import models
from datetime import datetime, timedelta


User = get_user_model()
today = datetime.now()
firstday = today.replace(day=1)
redirect_if_referer_not_found = '/'
# screenname = User

# if User.first_name


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


@login_required
def new_jobb(request):
    current_month = datetime.now().month
    last_month = datetime.now().month-1

    lastMonth = firstday - timedelta(days=1)
    this_month_timer = models.Timeliste.objects.filter(
        dato__month=current_month).order_by('dato')
    total_timer = this_month_timer.aggregate(Sum('timer'))
    last_month_timer = models.Timeliste.objects.filter(
        dato__month=last_month).order_by('dato')
    total_timer_lastmonth = last_month_timer.aggregate(Sum('timer'))
    jobbform = JobberForm(request.POST or None)
    timeform = TimelisteForm(request.POST or None)
    if request.method == "POST":
        if timeform.is_valid():
            timeform.instance.user = request.user
            timeform.save()
            messages.success(request, 'Timer Lagt til')
            return redirect(reverse("new_jobb"))

        elif jobbform.is_valid():
            jobbform.save()
            messages.success(request, 'Jobb Lagt til')
            return redirect(reverse("new_jobb"))
    context = {
        'jobbform': jobbform,
        'timeform': timeform,
        'total_timer': total_timer,
        'this_month_timer': this_month_timer,
        'last_month_timer': last_month_timer,
        'total_timer_lastmonth': total_timer_lastmonth,

        'lastMonth': lastMonth
    }

    return render(request, 'timelister/new_jobb.html', context)


def new_matriell(request):
    form = MatriellForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("new_matriell"))
    context = {
        'form': form
    }
    return render(request, 'timelister/new_matriell.html', context)


def timeliste(request):
    current_month = datetime.now().month
    this_month_timer = models.Timeliste.objects.filter(
        dato__month=current_month).filter(user=request.user).order_by('dato')
    total_timer = this_month_timer.aggregate(Sum('timer'))
    timeform = TimelisteForm(request.POST or None)

    if request.method == "POST":
        if timeform.is_valid():
            timeform.instance.user = request.user
            timeform.save()
            messages.success(request, 'Timer Lagt til')
            # return redirect(reverse("timelister"))
            return redirect(reverse("timeliste"))

    context = {
        'timeform': timeform,
        'total_timer': total_timer,
        'this_month_timer': this_month_timer,
    }
    return render(request, 'timelister/timeliste.html', context)


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


def timerDelete(request, object_id):
    object = get_object_or_404(models.Timeliste, pk=object_id)
    object.delete()
    messages.warning(request, 'Timer deleted.')

    # return redirect(reverse("new_jobb"))
    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))


def test(request):
    current_month = datetime.now().month
    this_month_timer = models.Timeliste.objects.filter(
        dato__month=current_month).order_by('dato')
    total_timer = this_month_timer.aggregate(Sum('timer'))
    timeform = TimelisteForm(request.POST or None)

    if request.method == "POST":
        if timeform.is_valid():
            timeform.instance.user = request.user
            timeform.save()
            messages.success(request, 'Timer Lagt til')
            return redirect(reverse("new_jobb"))

    context = {
        'timeform': timeform,
        'total_timer': total_timer,
        'this_month_timer': this_month_timer,
    }
    return render(request, 'timelister/test.html', context)
