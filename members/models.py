from django.db import models


class TestPem(models.Model):
    """Model definition for Test."""
    title = models.CharField(max_length=100, blank=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Test."""

        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def __str__(self):
        """Unicode representation of Test."""
        return self.title
