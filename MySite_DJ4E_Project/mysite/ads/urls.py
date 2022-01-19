from django.urls import path

from . import views

app_name = 'ads'
urlpatterns = [
    # ex: /ads/
    path('', views.AdListView.as_view(), name='index'),
    # ex: /ads/detail/2161
    path('ad/<int:pk>/detail', views.AdDetailView.as_view(), name='ad detail'),
    # ex: /ads/create
    path('create', views.AdCreateView.as_view(), name='ad create'),
    # ex: /ads/update/2161
    path('<int:pk>/update', views.AdUpdateView.as_view(), name='ad update'),
    # ex: /ads/delete/2161
    path('<int:pk>/delete', views.AdDeleteView.as_view(), name='ad delete'),
    # Ad File Stream
    path('ad_picture/<int:pk>', views.stream_file, name='ad picture'),
    # ex: /ads/2161/comment
    path('<int:pk>/comment', views.CommentCreateView.as_view(), name='ad comment create'),
    # ex: /ads/comment/2161/delete
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='ad comment delete'),
    # ex: /ads/2161/favorite
    path('<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad favorite'),
    # ex: /ads/2161/unfavorite
    path('<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad unfavorite'),
    ]
