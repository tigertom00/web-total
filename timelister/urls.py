from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.timeliste, name="timeliste"),
    path('timerlastmonth/', views.timelisteLastmonth,
         name="timerlastmonth"),
    path('jobblist/', views.jobblist, name="jobblist"),
    path('jobb/<jobb_id>/', views.jobbdetail, name='jobbdetail'),
    path('jobb/<jobb_id>/jobb-matriell',
         views.jobbMatriell, name='jobb-matriell'),
    path('matriell-list/', views.matriellList, name="matriell-list"),
    path('addmatriell/<jobb_id>/<object_id>/<antall>/',
         views.add_matriell, name='add-matriell'),
    path('deletematriell/<jobb_id>/<object_id>/<antall>/',
         views.delete_matriell, name='delete-matriell'),
    path('matriell/<object_id>',
         views.matriellDetail, name="matriell-detail"),
    path('transfmatriell/<jobb_id>/<object_id>/<transf>/',
         views.transf_matriell, name='transf-matriell'),
    re_path(r'^ny_timeliste/$', views.new_timeliste, name="new_timeliste"),

    re_path(r'^ny_jobb/$', views.new_jobb, name="new_jobb"),
    re_path(r'^(?P<object_id>[0-9]+)/delete_timer/$',
            views.timerDelete, name='delete_timer'),
    re_path(r'^(?P<object_id>[0-9]+)/delete_jobber/$',
            views.jobberDelete, name='delete_jobber'),
    re_path(r'^(?P<object_id>[0-9]+)/delete_matriell/$',
            views.matriellDelete, name='delete_matriell'),
    path('timermodal/', views.ModalTimerView.as_view(), name='modal-timer'),
]
