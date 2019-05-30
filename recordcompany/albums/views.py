from rest_framework import generics

from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Song.objects.filter(album_id=self.kwargs['pk'])
        return queryset

    serializer_class = SongSerializer


class SongDetail(generics.RetrieveDestroyAPIView):
    def get_queryset(self):
        queryset = Song.objects.filter(album_id=self.kwargs['album_pk'], id=self.kwargs['pk'])
        return queryset

    serializer_class = SongSerializer
