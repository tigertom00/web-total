from django.urls import path, include, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.timeliste, name="timeliste"),
    re_path(r'^timerlastmonth/$', views.timelisteLastmonth,
            name="timerlastmonth"),
    re_path(r'^jobblist/$', views.jobblist, name="jobblist"),
    path('jobb/<object_id>/', views.jobbdetail, name='jobbdetail'),
    re_path(r'^ny_timeliste/$', views.new_timeliste, name="new_timeliste"),
    re_path(r'^matriell/$', views.matriellList, name="matriell-list"),
    re_path(r'^ny_jobb/$', views.new_jobb, name="new_jobb"),
    re_path(r'^(?P<object_id>[0-9]+)/delete_timer/$',
            views.timerDelete, name='delete_timer'),
    re_path(r'^(?P<object_id>[0-9]+)/delete_jobber/$',
            views.jobberDelete, name='delete_jobber'),
]
