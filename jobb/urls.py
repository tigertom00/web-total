from django.urls import path
from . import views


urlpatterns = [
    path('', views.jobblist, name="jobblist"),
    path('<jobb_id>/', views.jobbdetail, name='jobbdetail'),
    path('<jobb_id>/edit/', views.editjobb, name='editjobb'),
    path('<jobb_id>/jobb-matriell',
         views.jobbMatriell, name='jobb-matriell'),
    path('<jobb_id>/delete-jobb',
         views.jobberDelete, name='delete_jobber'),
]
