from django import forms
from .models import Jobber


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
