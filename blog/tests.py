from django.test import TestCase
# from django.http import HttpRequest


# Create your tests here.
class HomePageTest(TestCase):
    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response=response, template_name='home_page.html')
