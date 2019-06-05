from rest_framework.test import APITestCase, APIRequestFactory

from .views import LabelViewSet


class TestLabel(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = LabelViewSet.as_view({'get': 'list'})
        self.uri = '/labels/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        status_code = response.status_code
        self.assertEqual(status_code, 200, 'Expected status 200, got {}'.format(status_code))
