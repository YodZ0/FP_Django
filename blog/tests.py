from django.test import TestCase
from blog.models import Article
from datetime import datetime
from django.http import HttpRequest
from blog.views import home_page, article_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response=response, template_name='home_page.html')

    def test_homepage_displays_articles(self):
        Article.objects.create(
            title='Article 1 title',
            summary='Article 1 summary',
            text='Article 1 text',
            category='Category 1',
            pub_date=datetime.now()
        )
        Article.objects.create(
            title='Article 2 title',
            summary='Article 2 summary',
            text='Article 2 text',
            category='Category 2',
            pub_date=datetime.now()
        )

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('UTF8')

        self.assertIn('Article 1 title', html)
        self.assertIn('/category/title-1', html)
        self.assertIn('Article 1 summary', html)
        self.assertNotIn('Article 1 text', html)

        self.assertIn('Article 2 title', html)
        self.assertIn('/category/title-2', html)
        self.assertIn('Article 2 summary', html)
        self.assertNotIn('Article 2 text', html)


class ArticlePageTest(TestCase):
    # def test_article_page_uses_correct_template(self):
    #     response = self.client.get('/')
    #     self.assertTemplateUsed(response=response, template_name='article_page.html')

    def test_article_page_displays_article(self):
        Article.objects.create(
            title='Article 1 title',
            summary='Article 1 summary',
            text='Article 1 text',
            category='Category 1',
            pub_date=datetime.now()
        )
        request = HttpRequest()
        response = article_page(request, 1)
        html = response.content.decode('UTF8')

        self.assertIn('Article 1 title', html)
        self.assertNotIn('Article 1 summary', html)
        self.assertIn('Article 1 text', html)


class ArticleModelTest(TestCase):
    def test_article_model_save_and_retrieve(self):
        # create Article 1
        article_1 = Article(
            title='Article 1',
            summary='Article 1 summary',
            text='Article 1 text',
            category='Article 1 category',
            pub_date=datetime.now(),
        )
        # save Article 1 in DB
        article_1.save()
        # create Article 2
        article_2 = Article(
            title='Article 2',
            summary='Article 2 summary',
            text='Article 2 text',
            category='Article 2 category',
            pub_date=datetime.now(),
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
        # check: second loaded == article 1
        self.assertEqual(articles[1].title, article_1.title)
