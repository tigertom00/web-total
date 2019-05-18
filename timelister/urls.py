from django.urls import path
from . import views


urlpatterns = [
    path('', views.timeliste, name="timeliste"),
    path('timerlastmonth/', views.timelisteLastmonth,
         name="timerlastmonth"),
    path('<object_id>/delete_timer/',
         views.timerDelete, name='delete_timer'),
    path('timermodal/', views.ModalTimerView.as_view(), name='modal-timer'),
]
