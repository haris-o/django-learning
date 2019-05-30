from rest_framework import generics, viewsets

from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
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
