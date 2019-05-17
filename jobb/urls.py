from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.jobblist, name="jobblist"),
    path('<jobb_id>/', views.jobbdetail, name='jobbdetail'),
    path('<jobb_id>/edit/', views.editjobb, name='editjobb'),
    path('<jobb_id>/bilder/', views.bilderjobb, name='bilderjobb'),
    path('<jobb_id>/jobb-matriell',
         views.jobbMatriell, name='jobb-matriell'),
    re_path(r'^(?P<object_id>[0-9]+)/delete_jobber/$',
            views.jobberDelete, name='delete_jobber'),
]
