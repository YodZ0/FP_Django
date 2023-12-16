from django.test import TestCase
from blog.models import Article, Categories
from datetime import datetime
from django.http import HttpRequest
from blog.views import home_page, article_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response=response, template_name='home_page.html')

    def test_homepage_displays_articles(self):
        category_1 = Categories.objects.create(
            category_name='category-1',
        )
        Article.objects.create(
            title='Article 1 title',
            summary='Article 1 summary',
            text='Article 1 text',
            category=category_1,
            pub_date=datetime.now(),
            slug='slug-1',
        )
        category_2 = Categories.objects.create(
            category_name='category-2',
        )
        Article.objects.create(
            title='Article 2 title',
            summary='Article 2 summary',
            text='Article 2 text',
            category=category_2,
            pub_date=datetime.now(),
            slug='slug-2',
        )

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('UTF8')

        self.assertIn('Article 1 title', html)
        self.assertIn('slug-1', html)
        self.assertIn('Article 1 summary', html)
        self.assertNotIn('Article 1 text', html)

        self.assertIn('Article 2 title', html)
        self.assertIn('slug-2', html)
        self.assertIn('Article 2 summary', html)
        self.assertNotIn('Article 2 text', html)


class ArticlePageTest(TestCase):
    # def test_article_page_uses_correct_template(self):
    #     response = self.client.get('/')
    #     self.assertTemplateUsed(response=response, template_name='article_page.html')

    def test_article_page_displays_article(self):
        category_1 = Categories.objects.create(
            category_name='category-1',
        )
        Article.objects.create(
            title='Article 1 title',
            summary='Article 1 summary',
            text='Article 1 text',
            category=category_1,
            pub_date=datetime.now(),
            slug='slug-1',
        )
        request = HttpRequest()
        response = article_page(request, 'slug-1')
        html = response.content.decode('UTF8')

        self.assertIn('Article 1 title', html)
        self.assertNotIn('Article 1 summary', html)
        self.assertIn('Article 1 text', html)


class ArticleModelTest(TestCase):
    def test_article_model_save_and_retrieve(self):
        # create category 1
        category_1 = Categories.objects.create(
            category_name='category-1',
        )
        # create Article 1
        article_1 = Article(
            title='Article 1',
            summary='Article 1 summary',
            text='Article 1 text',
            category=category_1,
            pub_date=datetime.now(),
            slug='slug-1',
        )
        # save Article 1 in DB
        article_1.save()
        # create category 2
        category_2 = Categories.objects.create(
            category_name='category-2',
        )
        # create Article 2
        article_2 = Article(
            title='Article 2',
            summary='Article 2 summary',
            text='Article 2 text',
            category=category_2,
            pub_date=datetime.now(),
            slug='slug-2',
        )
        # save Article 2 in DB
        article_2.save()
        # load all Articles from DB
        articles = Article.objects.all()
        articles = articles[::-1]
        # check: there is two (2) articles
        self.assertEqual(len(articles), 2)
        # check: first loaded == article 2
        self.assertEqual(articles[0].title, article_2.title)
        self.assertEqual(articles[0].slug, article_2.slug)
        self.assertEqual(articles[0].category, article_2.category)
        # check: second loaded == article 1
        self.assertEqual(articles[1].title, article_1.title)
        self.assertEqual(articles[1].slug, article_1.slug)
        self.assertEqual(articles[1].category, article_1.category)


class AboutPageTest(TestCase):
    def test_about_page_uses_correct_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response=response, template_name='about_page.html')


class ContactPageTest(TestCase):
    def test_contact_page_uses_correct_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response=response, template_name='contact_page.html')
