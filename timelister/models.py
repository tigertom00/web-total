from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from matriell.models import Matriell
from jobb.models import Jobber


User = get_user_model()


class Timeliste(models.Model):
    """Model definition for Timeliste."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobb = models.ForeignKey(Jobber, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    dato = models.DateField(null=True, blank=True)
    timer = models.SmallIntegerField(null=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Timeliste."""

        verbose_name = 'timeliste'
        verbose_name_plural = 'timelister'

    def __str__(self):
        """Unicode representation of Timeliste."""
        return self.jobb.tittel
