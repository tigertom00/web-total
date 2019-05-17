from django import forms
import datetime
from .models import TestImg, TestBlog

datenow = datetime.datetime.now()


class TestImgForm(forms.ModelForm):
    """Form definition for Testimg."""

    class Meta:
        """Meta definition for TestImgForm."""

        model = TestImg
        fields = ('title', 'img')


class TestBlogForm(forms.ModelForm):
    """Form definition for TestBlog."""

    class Meta:
        """Meta definition for TestBlogform."""

        model = TestBlog
        fields = ('title', 'body', 'profile_img')
