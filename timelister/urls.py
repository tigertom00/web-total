from django.urls import path, include, re_path
from . import views


urlpatterns = [
    re_path(r'^timeliste/$', views.timeliste, name="timeliste"),
    re_path(r'^timerlastmonth/$', views.timelisteLastmonth,
            name="timerlastmonth"),
    re_path(r'^test/$', views.test, name="test"),
    re_path(r'^ny_timeliste/$', views.new_timeliste, name="new_timeliste"),
    re_path(r'^ny_jobb/$', views.new_jobb, name="new_jobb"),
    re_path(r'^ny_matriell/$', views.new_matriell, name="new_matriell"),
    re_path(r'^(?P<object_id>[0-9]+)/delete_timer/$',
            views.timerDelete, name='delete_timer'),
]
