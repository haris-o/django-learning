from django.urls import path

from .views import AlbumList, AlbumDetail, SongList, SongDetail

urlpatterns = [
    path('albums/', AlbumList.as_view(), name='albums_list'),
    path('albums/<int:pk>/', AlbumDetail.as_view(), name='albums_detail'),
    path('albums/<int:pk>/songs/', SongList.as_view(), name='songs_list'),
    path('albums/<int:album_pk>/songs/<int:pk>/', SongDetail.as_view(), name='songs_detail')
]
