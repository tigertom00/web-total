from django import forms
from .models import Timeliste, Jobber, Matriell
from flatpickr import DatePickerInput
import datetime

datenow = datetime.datetime.now()


class TimelisteForm(forms.ModelForm):
    """Form definition for Timeliste."""
    timer = forms.CharField(max_length="2", initial="8", widget=forms.TextInput(
        attrs={
            'placeholder': '* Antall Timer...',
        }))
    dato = forms.DateField(required=True, initial=datenow,
                           widget=DatePickerInput())

    class Meta:
        """Meta definition for TimelisteForm."""

        model = Timeliste
        fields = (
            'jobb',
            'dato',
            'timer',
        )
        # widgets = {
        #     'dato': DatePickerInput(),
        # }


class JobberForm(forms.ModelForm):
    """Form definition for Jobber."""
    ordre_nr = forms.CharField(max_length=4, required=True, widget=forms.TextInput(
        attrs={
            'placeholder': '* Ordre nr...',
        }))
    tittel = forms.CharField(max_length=64, widget=forms.TextInput(
        attrs={
            'placeholder': '* Tittel...',
        }))
    adresse = forms.CharField(max_length=256, required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Adresse...',
        }))

    class Meta:
        """Meta definition for Jobberform."""

        model = Jobber
        fields = (
            'ordre_nr',
            'tittel',
            'adresse',

        )


class EditJobbForm(forms.ModelForm):
    """Form definition for EditJobb."""
    tittel = forms.CharField(max_length=64, widget=forms.TextInput(
        attrs={
            'placeholder': '* Tittel...',
        }))
    adresse = forms.CharField(max_length=256, required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Adresse...',
        }))
    telefon_nr = forms.CharField(max_length=64, required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Telefon nr...',
        }))
    beskrivelse = forms.TextInput

    class Meta:
        """Meta definition for EditJobbform."""

        model = Jobber
        fields = (
            'tittel',
            'adresse',
            'telefon_nr',
            'beskrivelse',
        )


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
