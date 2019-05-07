from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from . import views
from timelister import views as time_views

urlpatterns = [
    re_path(r'^$', login_required(views.home), name='home'),
    re_path(r'^profile/$', login_required(views.profile), name='profile'),

]
