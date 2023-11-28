import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicInstallTest(unittest.TestCase):
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

    def test_homepage_shows_articles(self):
        self.browser.get('http://localhost:8000')
        # Also he saw all articles with title and description (short) there
        container = self.browser.find_element(By.CLASS_NAME, 'container')

        article_title = container.find_element(By.CLASS_NAME, 'article-title')
        article_summary = container.find_element(By.CLASS_NAME, 'article-summary')
        article_text = container.find_element(By.CLASS_NAME, 'article-text')

        self.assertTrue(article_title)
        self.assertTrue(article_summary)
        self.assertFalse(article_text)


if __name__ == '__main__':
    unittest.main()

# <<<---- Experience usage story ---->>>
# There was a top-bar menu with buttons: Blog, About
# and sidebar with categories: Programming, English, Other

# When he scrolled down, he saw 10 articles before bot-bar menu with pagination
# that allows to choose current page

# Then he saw footer with copyrighting and other info

# When he clicked on article title he moved to article page

# On article page he saw a title, category, and article text
# A title of this article page was article title

# >>>---- Experience usage story ----<<<
