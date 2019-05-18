from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


User = get_user_model()


class Leverandorer(models.Model):
    name = models.CharField(max_length=64, blank=True)
    """Model definition for Leverandorer."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Leverandorer."""

        verbose_name = 'Leverandor'
        verbose_name_plural = 'Leverandorer'

    def __str__(self):
        """Unicode representation of Leverandorer."""
        return self.name


class Matriell(models.Model):
    """Model definition for Matriell."""
    el_nr = models.IntegerField(unique=True, blank=True, null=True,)
    tittel = models.CharField(max_length=64, unique=True, blank=True)
    info = models.CharField(max_length=256, blank=True)
    leverandor = models.ForeignKey(
        Leverandorer, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(
        upload_to='matriell_image', default='default/matriell.png')
    # TODO: Define fields here

    class Meta:
        """Meta definition for Matriell."""

        verbose_name = 'Matriell'
        verbose_name_plural = 'Matriell'

    def __str__(self):
        """Unicode representation of Matriell."""
        return self.tittel

    def get_absolute_url(self):
        return reverse('matriell-detail', kwargs={'pk': self.pk})
