from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from matriell.models import Matriell


User = get_user_model()


class JobbMatriell(models.Model):
    """Model definition for Matriell."""
    matriell = models.ForeignKey(Matriell, on_delete=models.CASCADE)
    antall = models.IntegerField(default=1)
    jobb = models.ForeignKey('Jobber', on_delete=models.CASCADE)
    transf = models.BooleanField(default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Matriell."""

        verbose_name = 'JobbMatriell'
        verbose_name_plural = 'JobbMatriell'

    def __str__(self):
        """Unicode representation of Matriell."""
        return self.matriell.tittel


class Jobber(models.Model):
    """Model definition for Jobber."""
    ordre_nr = models.PositiveSmallIntegerField(primary_key=True)
    tittel = models.CharField(max_length=64, unique=True, blank=True)
    adresse = models.CharField(max_length=256, blank=True)
    telefon_nr = models.CharField(max_length=64, blank=True)
    beskrivelse = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    ferdig = models.BooleanField(default=False)
    matriell = models.ManyToManyField(JobbMatriell, blank=True)

    # TODO: Define fields here
    # Koble til timer og matriell
    class Meta:
        """Meta definition for Jobber."""

        verbose_name = 'Jobb'
        verbose_name_plural = 'Jobber'

    def __str__(self):
        """Unicode representation of Jobber."""
        return self.tittel
