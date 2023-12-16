import unittest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

# Imitation of user actions


class AboutPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_about_page_looks_correct(self):
        self.browser.get(self.live_server_url)
        about = self.browser.find_element(By.CLASS_NAME, 'nav-about')
        self.browser.get(about.get_attribute('href'))
        self.assertEqual('About', self.browser.title)


class ContactPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_about_page_looks_correct(self):
        self.browser.get(self.live_server_url)
        about = self.browser.find_element(By.CLASS_NAME, 'nav-contact')
        self.browser.get(about.get_attribute('href'))
        self.assertEqual('Contact', self.browser.title)


class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_homepage_title(self):
        # Tima has heard about cool web blog called "Solo-leveling with ChatGPT"
        # He tried to visit that site
        self.browser.get(self.live_server_url)
        # He saw a page with title "Solo-leveling with ChatGPT"
        self.assertIn('Solo-leveling with ChatGPT', self.browser.title)

    def test_homepage_header(self):
        self.browser.get(self.live_server_url)
        # He saw main header "Blog about usage of ChatGPT in self-improvement"
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual('Solo-leveling with ChatGPT', header)

    def test_homepage_has_articles(self):
        self.browser.get(self.live_server_url)
        # Also he saw all articles
        self.assertTrue(self.browser.find_element(By.CLASS_NAME, 'articles-list'))

    def test_homepage_article_looks_correct(self):
        # There is an Articles with title, summary, category and publication date
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        article_category = self.browser.find_element(By.CLASS_NAME, 'article-category')
        article_pubdate = self.browser.find_element(By.CLASS_NAME, 'article-pubdate')

        self.assertTrue(article_title)
        self.assertTrue(article_summary)
        self.assertTrue(article_category)
        self.assertTrue(article_pubdate)

    def test_homepage_article_title_link_leads_to_article_page(self):
        # Timur clicked on Article title and get article page with full text
        # open home page
        self.browser.get(self.live_server_url)
        # find article title
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        # find a link in the article title
        article_title_link = article_title.find_element(By.TAG_NAME, 'a')
        # follow the link
        self.browser.get(article_title_link.get_attribute('href'))
        # check if opened page correct article title
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        self.assertEqual(article_title.text, self.browser.find_element(By.CLASS_NAME, 'article-title').text)


class ArticlePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_article_page_looks_correct(self):
        # Timur find an article on home page
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_title_text = article_title.text
        article_title_link = article_title.find_element(By.TAG_NAME, 'a')
        # He follows an article
        self.browser.get(article_title_link.get_attribute('href'))
        # Article page has article title
        self.assertEqual(article_title_text, self.browser.title)
        # article text
        self.assertTrue(self.browser.find_element(By.CLASS_NAME, 'article-text'))
        # article category
        self.assertTrue(self.browser.find_element(By.CLASS_NAME, 'article-category'))
        # article pubdate
        self.assertTrue(self.browser.find_element(By.CLASS_NAME, 'article-pubdate'))


class CategoriesPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

# <<<---- Experience usage story ---->>>

# There is also an update date under Article if it was updated

# There was a top-bar menu with buttons: Home, About, Categories, Contact

# On click on Home, opens Home page
# On click on About, opens About page
# On click on Contact, opens Contact page

# On click on Categories, opens Categories page with categories list with links /categories
# On click on category, opens page with all articles that have same category /category

# When he scrolled down, he saw 10 articles before bot-bar menu with pagination
# that allows to choose current page

# Timur tries to open non-existent article, and he saw 404 page

# >>>---- Experience usage story ----<<<
