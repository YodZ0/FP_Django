from django.db import models
from django.urls import reverse

# Create your models here.


class Categories(models.Model):
    # английский язык, маркетинг, краткое содержание книг, спортивные программы, ИИ, программирование
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500)
    text = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    pub_date = models.DateField()
    slug = models.CharField(max_length=255, unique=True)
    # TODO
    # upd_date = models.DateTimeField(auto_now=True)
    # is_published = models.BooleanField()

    def __str__(self):
        return f'{self.title}, {self.category}'

    def get_absolute_url(self):
        return reverse('article_page', kwargs={'slug': self.slug})
        # return reverse('article_page',
        #                kwargs={
        #                    'category': self.category,
        #                    'slug': self.slug,
        #                })
