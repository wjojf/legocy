from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import MarketItem


class LoginTest(APITestCase):
    fixtures = ['test_db.json']

    def setUp(self) -> None:
        """Setting up LoginTest"""
        self.user = User.objects.get(username='test_user')
        self.market_item = MarketItem.objects.get(id=1)
        self.client = APIClient()
        self.client.force_login(self.user)
        super().setUp()

    def test_updating_market_item(self):
        data = {
            'id': self.market_item.id,
            'price': 200,
            'active': 'false',
            'currency': 'USD'
        }
        response = self.client.post(
            reverse('update-market-item', kwargs={'pk': self.market_item.id}),
            data=data,
            format='json'
        )
        new_market_item = MarketItem.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_market_item.price, data['price'])
        self.assertEqual(new_market_item.active, data['active'])
        self.assertEqual(new_market_item.currency, data['currency'])

