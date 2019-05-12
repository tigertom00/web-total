from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.matriellList, name="matriell-list"),
    path('<object_id>',
         views.matriellDetail, name="matriell-detail"),
    path('addmatriell/<jobb_id>/<object_id>/<antall>/',
         views.add_matriell, name='add-matriell'),
    path('deletematriell/<jobb_id>/<object_id>/<antall>/',
         views.delete_matriell, name='delete-matriell'),
    path('transfmatriell/<jobb_id>/<object_id>/<transf>/',
         views.transf_matriell, name='transf-matriell'),
    re_path(r'^(?P<object_id>[0-9]+)/delete_matriell/$',
            views.matriellDelete, name='delete_matriell'),
]
