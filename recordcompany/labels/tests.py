from rest_framework.test import APITestCase, APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .views import LabelViewSet


class TestLabel(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = LabelViewSet.as_view({'get': 'list'})
        self.uri = '/labels/'

        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='test@test.com',
            password='test'
        )

    def test_list(self):
        request = self.factory.get(
            self.uri,
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key)
        )
        request.user = self.user
        response = self.view(request)
        status_code = response.status_code
        self.assertEqual(status_code, 200, 'Expected status 200, got {}'.format(status_code))
