from django.test import TestCase
from django.urls import reverse

from .models import Product


class StoreViewTests(TestCase):
    def test_store_page_lists_products(self):
        Product.objects.create(
            name='Aurelius Chrono',
            short_description='A refined steel chronograph.',
            price='699.00',
            image_url='https://images.unsplash.com/photo-1523170335258-f5ed11844a49?auto=format&fit=crop&w=700&q=80',
            category='Chronograph',
            is_featured=True,
        )

        response = self.client.get(reverse('store'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aurelius Chrono')
