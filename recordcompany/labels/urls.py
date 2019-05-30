from django.urls import path

from .views import LabelList, LabelDetail

urlpatterns = [
    path('', LabelList.as_view(), name='labels_list'),
    path('<int:pk>/', LabelDetail.as_view(), name='labels_detail'),
]
