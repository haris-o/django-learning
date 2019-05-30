from rest_framework import generics

from .models import Label
from .serializers import LabelSerializer


class LabelList(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetail(generics.RetrieveDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
