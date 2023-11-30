import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_homepage_title(self):
        # Tima has heard about cool web blog called "Solo-leveling with ChatGPT"
        # He tried to visit that site
        self.browser.get('http://localhost:8000')
        # He saw a page with title "Solo-leveling with ChatGPT"
        self.assertIn('Solo-leveling with ChatGPT', self.browser.title)

    def test_homepage_header(self):
        self.browser.get('http://localhost:8000')
        # He saw main header "Blog about usage of ChatGPT in self-improvement"
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual('Blog about usage of ChatGPT in self-improvement', header)

    def test_homepage_has_articles(self):
        self.browser.get('http://localhost:8000')
        # Also he saw all articles
        self.assertTrue(self.browser.find_element(By.CLASS_NAME, 'articles-list'))

    def test_homepage_article_look_correct(self):
        # There is an Articles with title, summary, category and publication date
        self.browser.get('http://localhost:8000')
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        article_category = self.browser.find_element(By.CLASS_NAME, 'article-category')

        self.assertTrue(article_title)
        self.assertTrue(article_summary)
        self.assertTrue(article_category)


if __name__ == '__main__':
    unittest.main()

# <<<---- Experience usage story ---->>>
# There is also an update date under Article

# There was a top-bar menu with buttons: Blog, About
# and sidebar with categories: Programming, English, Other

# When he scrolled down, he saw 10 articles before bot-bar menu with pagination
# that allows to choose current page

# Then he saw footer with copyrighting and other info

# When he clicked on article title he moved to article page

# On article page he saw a title, category, and article text
# A title of this article page was article title

# >>>---- Experience usage story ----<<<
