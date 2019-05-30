from rest_framework import generics

from .models import Artist
from .serializers import ArtistSerializer, UserSerializer


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
