from django.urls import path

from . import views

app_name = 'autos'
urlpatterns = [
    # ex: /autos/
    path('', views.AutoIndex.as_view(), name='index'),
    # ex: /autos/auto/create
    path('auto/create/', views.AutoCreate.as_view(), name='auto create'),
    # ex: /autos/auto/update/3
    path('auto/update/<int:pk>/', views.AutoUpdate.as_view(), name='auto update'),
    # ex: /autos/auto/delete/5
    path('auto/delete/<int:pk>/', views.AutoDelete.as_view(), name='auto delete'),
    # ex: /autos/make
    path('make', views.MakeList.as_view(), name='make list'),
    # ex: /autos/make/create
    path('make/create/', views.MakeCreate.as_view(), name='make create'),
    # ex: /autos/make/update/3
    path('make/update/<int:pk>/', views.MakeUpdate.as_view(), name='make update'),
    # ex: /autos/make/delete/5
    path('make/delete/<int:pk>/', views.MakeDelete.as_view(), name='make delete'),
]