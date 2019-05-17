from django.db import models


class TestImg(models.Model):
    """Model definition for TestImg."""
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='testing')

    # TODO: Define fields here

    class Meta:
        """Meta definition for TestImg."""

        verbose_name = 'TestImg'
        verbose_name_plural = 'TestImgs'

    def __str__(self):
        """Unicode representation of TestImg."""
        return self.title


class TestBlog(models.Model):
    """Model definition for TestBlog."""
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='tesing/blog')

    # TODO: Define fields here

    class Meta:
        """Meta definition for TestBlog."""

        verbose_name = 'TestBlog'
        verbose_name_plural = 'TestBlogs'

    def __str__(self):
        """Unicode representation of TestBlog."""
        return self.title
