from django.shortcuts import redirect, reverse, get_object_or_404, render
from django.http import HttpResponse

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Sum, Count
from .forms import MatriellForm
from timelister import models as t_models
from jobb import models as j_models
from . import models
from datetime import datetime, timedelta
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy

User = get_user_model()
today = datetime.now()
firstday = today.replace(day=1)
redirect_if_referer_not_found = '/'


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
    jobb = get_object_or_404(t_models.Jobber, pk=jobb_id)
    jobb_matriell, created = j_models.JobbMatriell.objects.get_or_create(
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
    jobb = get_object_or_404(t_models.Jobber, pk=jobb_id)
    jobb_matriell = j_models.JobbMatriell.objects.get(
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
    jobb = get_object_or_404(t_models.Jobber, pk=jobb_id)
    jobb_matriell = j_models.JobbMatriell.objects.get(
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
