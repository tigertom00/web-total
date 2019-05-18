from django.shortcuts import redirect, reverse, get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import MatriellForm, EditMatriellForm
from timelister import models as t_models
from jobb import models as j_models
from . import models

redirect_if_referer_not_found = '/'
# TODO: Delete transfered matriell from jobb


# leverandor liste
@login_required
def leverandorList(request):
    leverandor = models.Leverandorer.objects.all()
    leverandorform = LeverandorerForm(request.POST or None)
    if request.method == "POST":
        if leverandor.is_valid():
            leverandor.save()
            messages.success(request, 'Leveranør Lagt til')
            return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))
    context = {
        'leverandor': leverandor,
        'leverandorform': leverandorform
    }
    return render(request, 'matriell/leverandor-liste.html', context)


# Delete Leverandorer from Leverandorer list
@login_required
def leveranorDelete(request, lev_id):
    leverandor = get_object_or_404(models.Leverandorer, pk=lev_id)
    leverandor.delete()
    messages.warning(request, 'Leverandor deleted.')
    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))


# Matriell List View
@login_required
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
    return render(request, 'matriell/matiell-liste.html', context)


# Matriell Detail View
@login_required
def matriellDetail(request, object_id):
    matriell = get_object_or_404(models.Matriell, pk=object_id)
    context = {
        'matriell': matriell,
    }
    return render(request, 'matriell/matriell-detail.html', context)


# Edit Matriell
@login_required
def editMatriell(request, object_id):
    matriell = get_object_or_404(models.Matriell, pk=object_id)
    if request.method == "POST":
        editmatriell = EditMatriellForm(request.POST,
                                        request.FILES, instance=matriell)
        if editmatriell.is_valid():
            editmatriell.save()
            messages.success(request, 'Matriell oppdatert')
            return redirect(reverse("matriell-detail", kwargs={
                'object_id': object_id
            }))
    editmatriell = EditMatriellForm(instance=matriell)
    context = {
        'matriell': matriell,
        'editmatriell': editmatriell,
    }
    return render(request, 'matriell/edit-matriell.html', context)


# Delete Matriell from matriell list
@login_required
def matriellDelete(request, object_id):
    matriell = get_object_or_404(models.Matriell, pk=object_id)
    matriell.delete()
    messages.warning(request, 'Matriell deleted.')
    return redirect(request.META.get('HTTP_REFERER', redirect_if_referer_not_found))


# Add Matriell to jobb
@login_required
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
@login_required
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
@login_required
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
