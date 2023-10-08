from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=100, inventory=100)

    def test_get_all(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
