from django.urls import path

from . import views

app_name = 'cats'
urlpatterns = [
    # ex: /cats/
    path('', views.CatIndex.as_view(), name='index'),
    # ex: /cats/cat/create
    path('cat/create', views.CatCreate.as_view(), name='cat create'),
    # ex: /cats/cat/update/2161
    path('cat/update/<int:pk>', views.CatUpdate.as_view(), name='cat update'),
    # ex: /cats/cat/delete/2161
    path('cat/delete/<int:pk>', views.CatDelete.as_view(), name='cat delete'),
    # ex: /cats/breeds
    path('breeds/', views.BreedList.as_view(), name='breed list'),
    # ex: /cats/breed/create
    path('breed/create', views.BreedCreate.as_view(), name='breed create'),
    # ex: /cats/breed/update/2161
    path('breed/update/<int:pk>', views.BreedUpdate.as_view(), name='breed update'),
    # ex: /cats/breed/delete/2161
    path('breed/delete/<int:pk>', views.BreedDelete.as_view(), name='breed delete')
    ]