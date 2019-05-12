from django import forms
from .models import Timeliste
from flatpickr import DatePickerInput
from bootstrap_modal_forms.forms import BSModalForm
import datetime

datenow = datetime.datetime.now()


class ModalTimerForm(BSModalForm):

    class Meta:

        model = Timeliste
        fields = (
            'jobb',
            'dato',
            'timer',
        )


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
