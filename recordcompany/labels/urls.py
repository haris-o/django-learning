from django.urls import path

from .views import LabelList, LabelDetail

urlpatterns = [
    path('labels/', LabelList.as_view(), name='labels_list'),
    path('labels/<int:pk>/', LabelDetail.as_view(), name='labels_detail'),
]
