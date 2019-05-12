from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.timeliste, name="timeliste"),
    path('timerlastmonth/', views.timelisteLastmonth,
         name="timerlastmonth"),


    re_path(r'^ny_timeliste/$', views.new_timeliste, name="new_timeliste"),

    re_path(r'^ny_jobb/$', views.new_jobb, name="new_jobb"),
    re_path(r'^(?P<object_id>[0-9]+)/delete_timer/$',
            views.timerDelete, name='delete_timer'),


    path('timermodal/', views.ModalTimerView.as_view(), name='modal-timer'),
]
