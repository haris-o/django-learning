from rest_framework.routers import DefaultRouter

from .views import LabelViewSet

router = DefaultRouter()
router.register('labels', LabelViewSet, base_name='labels')

urlpatterns = router.urls
