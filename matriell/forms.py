from django import forms
from .models import Matriell, Leverandorer


class MatriellForm(forms.ModelForm):
    """Form definition for Matriell."""
    el_nr = forms.CharField(max_length=7, widget=forms.TextInput(
        attrs={
            'placeholder': 'El nr...',
        }))
    tittel = forms.CharField(max_length=64, widget=forms.TextInput(
        attrs={
            'placeholder': '* Tittel...',
        }))

    info = forms.CharField(max_length=256, required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Mer info...',
        }))

    class Meta:
        """Meta definition for Matriellform."""

        model = Matriell

        fields = (
            'el_nr',
            'tittel',
            'leverandor',
            'info',
        )


class EditMatriellForm(forms.ModelForm):

    class Meta:
        model = Matriell
        fields = (
            'el_nr',
            'tittel',
            'leverandor',
            'info',
            'image',
        )


class LeverandorerForm(forms.ModelForm):
    name = forms.CharField(max_length=64, widget=forms.TextInput(
        attrs={
            'placeholder': '* Navn...',
        }))

    class Meta:
        model = Leverandorer
        fields = ('name',)
