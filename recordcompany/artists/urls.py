from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ArtistViewSet, UserCreate, UserLogin

router = DefaultRouter()
router.register('artists', ArtistViewSet, base_name='artists')

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', UserLogin.as_view(), name='user_login')
]

urlpatterns += router.urls
