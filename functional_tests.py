import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_install(self):
        # Tima has heard about cool web blog called "Solo-leveling with ChatGPT"
        # He tried to visit that site
        self.browser.get("http://localhost:8000")

        # He saw a page with title "Solo-leveling with ChatGPT"
        self.assertIn("Solo-leveling with ChatGPT", self.browser.title)


if __name__ == '__main__':
    unittest.main()

# <<<---- Experience usage story ---->>>

# logo and main header "Blog about usage of ChatGPT in self-improvement"

# Also he saw all articles with title and description (short) there

# There was a top-bar menu with buttons: Blog, About
# and sidebar with categories: Programming, English, Other

# When he scrolled down, he saw 10 articles before bot-bar menu with pagination
# that allows to choose current page

# Then he saw footer with copyrighting and other info

# When he clicked on article title he moved to article page

# On article page he saw a title, category, and article text
# A title of this article page was article title

# >>>---- Experience usage story ----<<<
