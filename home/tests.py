from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify
# Create your tests here.
class HomeTestCase(TestCase):
    def test_home(self):
        response = self.client.get(reverse('articles:home'))
        self.assertEqual(response.status_code, 200)   

    def test_create_page(self):
        response = self.client.get(reverse('articles:create'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('articles:create'), 
        {'title': 'Test item',
        'content': 'This is a test item.'})

        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        slg = slugify('Test item')
        response = self.client.get(reverse("articles:detail", kwargs={"slug": slg}))
        self.assertEqual(response.status_code, 200)
    
