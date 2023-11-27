from django.test import TestCase
from django.http import HttpRequest
from blog.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_homepage_return_correct_url(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>Solo-leveling with ChatGPT</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))

    def test_homepage_return_correct_url_2(self):
        response = self.client.get("/")
        self.assertContains(response=response, text="<title>Solo-leveling with ChatGPT</title>")
