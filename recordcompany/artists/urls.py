from django.urls import path

from .views import ArtistList, ArtistDetail, UserCreate

urlpatterns = [
    path('artists/', ArtistList.as_view(), name='artists_list'),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name='artists_detail'),
    path('users/', UserCreate.as_view(), name='user_create')
]
