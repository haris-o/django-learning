from rest_framework import viewsets

from .models import Label
from .serializers import LabelSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
