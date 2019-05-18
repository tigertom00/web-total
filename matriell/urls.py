from django.urls import path
from . import views


urlpatterns = [

    path('', views.matriellList, name="matriell-list"),
    path('leverandor/', views.leverandorList, name='leverandor-list'),
    path('leverandor/<lev_id>/',
         views.leveranorDelete, name='delete_leveranor'),
    path('<object_id>/', views.matriellDetail, name="matriell-detail"),
    path('<object_id>/edit/', views.editMatriell, name="editmatriell"),
    path('delete_matriell/<object_id>/',
         views.matriellDelete, name='delete_matriell'),
    path('addmatriell/<jobb_id>/<object_id>/<antall>/',
         views.add_matriell, name='add-matriell'),
    path('deletematriell/<jobb_id>/<object_id>/<antall>/',
         views.delete_matriell, name='delete-matriell'),
    path('transfmatriell/<jobb_id>/<object_id>/<transf>/',
         views.transf_matriell, name='transf-matriell'),

]
