from django.urls import path, include, re_path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    re_path(r'^$', login_required(views.secret), name="secret"),
]
