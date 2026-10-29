from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Booking, MenuItem

User = get_user_model()

class RestaurantAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_url = "/restaurant/menu/"
        self.booking_url = "/restaurant/booking/"
        self.registration_url = "/restaurant/registration/"
        self.token_url = "/restaurant/api-token-auth/"

    def test_menu_list_is_public(self):
        MenuItem.objects.create(title="Greek salad", price="12.50", inventory=10)
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Greek salad")

    def test_anonymous_cannot_create_menu_item(self):
        response = self.client.post(self.menu_url, {"title": "Pasta", "price": "14.00", "inventory": 5}, format="json")
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_create_menu_item(self):
        user = User.objects.create_user(username="tester", password="StrongPass123!")
        self.client.force_authenticate(user=user)
        response = self.client.post(self.menu_url, {"title": "Pasta", "price": "14.00", "inventory": 5}, format="json")
        self.assertEqual(response.status_code, 201)

    def test_booking_list_and_create_permission(self):
        Booking.objects.create(first_name="Sam", reservation_date="2030-01-01", reservation_slot="18:00")
        self.assertEqual(self.client.get(self.booking_url).status_code, 200)
        user = User.objects.create_user(username="booker", password="StrongPass123!")
        self.client.force_authenticate(user=user)
        response = self.client.post(self.booking_url, {"first_name": "Alex", "reservation_date": "2030-01-02", "reservation_slot": "19:00"}, format="json")
        self.assertEqual(response.status_code, 201)

    def test_registration_and_token_login(self):
        response = self.client.post(self.registration_url, {"username": "newuser", "email": "new@example.com", "password": "StrongPass123!"}, format="json")
        self.assertEqual(response.status_code, 201)
        response = self.client.post(self.token_url, {"username": "newuser", "password": "StrongPass123!"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)
