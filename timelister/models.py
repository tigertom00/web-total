from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Jobber(models.Model):
    """Model definition for Jobber."""
    ordre_nr = models.PositiveSmallIntegerField(primary_key=True)
    tittel = models.CharField(max_length=64, blank=True)
    adresse = models.CharField(max_length=256, blank=True)
    telefon_nr = models.CharField(max_length=64, blank=True)
    beskrivelse = models.CharField(max_length=256, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Jobber."""

        verbose_name = 'Jobb'
        verbose_name_plural = 'Jobber'

    def __str__(self):
        """Unicode representation of Jobber."""
        return self.tittel


class Matriell(models.Model):
    """Model definition for Matriell."""
    el_nr = models.IntegerField(blank=True, null=True,)
    jobb = models.ForeignKey(Jobber, on_delete=models.CASCADE)
    beskrivelse = models.CharField(max_length=128, blank=True)
    Leverandor = models.CharField(max_length=128, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Matriell."""

        verbose_name = 'Matriell'
        verbose_name_plural = 'Matriell'

    def __str__(self):
        """Unicode representation of Matriell."""
        return self.beskrivelse


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
