from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.testimg, name="testing"),
    path('testblog_c/', views.testblog_c, name="testblog_c"),
    path('testblog_l/', views.testblog_l, name="testblog_l"),
    path('testblog/<blog_id>/', views.testblog, name="testblog"),
    path('edittestblog/<blog_id>/', views.edittestblog, name="edittestblog"),
]
