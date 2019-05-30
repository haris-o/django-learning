from django.urls import path

from .views import ArtistList, ArtistDetail

urlpatterns = [
    path('', ArtistList.as_view(), name='artists_list'),
    path('<int:pk>/', ArtistDetail.as_view(), name='artists_detail')
]
