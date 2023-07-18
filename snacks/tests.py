from django.test import SimpleTestCase
from django.urls import reverse


class ThingsTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    # def test_false_page_status_code(self):
    #     url_invalid = reverse('invalid_path')
    #     response_invalid = self.client.get(url_invalid)
    #     self.assertEqual(response_invalid.status_code, 404)

    def test_home_page_templete(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_templete(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')