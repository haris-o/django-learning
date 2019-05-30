from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AlbumViewSet, SongList, SongDetail

router = DefaultRouter()
router.register('albums', AlbumViewSet, base_name='albums')

urlpatterns = [
    path('albums/<int:pk>/songs/', SongList.as_view(), name='songs_list'),
    path('albums/<int:album_pk>/songs/<int:pk>/', SongDetail.as_view(), name='songs_detail')
]

urlpatterns += router.urls
