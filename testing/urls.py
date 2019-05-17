from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.testimg, name="testing"),
    path('testblog_c', views.testimg, name="testing"),
    path('', views.testimg, name="testing"),
    path('', views.testimg, name="testing"),
]
