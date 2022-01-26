from django.urls import path

from . import views

app_name = 'ads'
urlpatterns = [
    # ex: /ads/
    path('', views.AdListView.as_view(), name='index'),
    # ex: /ads/detail/2161
    path('detail/<int:pk>', views.AdDetailView.as_view(), name='ad detail'),
    # ex: /ads/create
    path('create', views.AdCreateView.as_view(), name='ad create'),
    # ex: /ads/update/2161
    path('update/<int:pk>', views.AdUpdateView.as_view(), name='ad update'),
    # ex: /ads/delete/2161
    path('delete/<int:pk>', views.AdDeleteView.as_view(), name='ad delete'),
    # Ad File Stream
    path('ad_picture/<int:pk>', views.stream_file, name='ad picture'),
    # ex: /ads/2161/comment
    path('<int:pk>/comment', views.CommentCreateView.as_view(), name='ad comment create'),
    # ex: /ads/comment/2161/delete
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='ad comment delete'),
    # ex: /ads/favorite/2161
    path('<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad favorite'),
    # ex: /ads/unfavorite/2161
    path('unfavorite/<int:pk>', views.DeleteFavoriteView.as_view(), name='ad unfavorite'),
    ]
