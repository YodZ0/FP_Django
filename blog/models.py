from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500)
    text = models.TextField()
    category = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    # TODO
    # category -> create new model -> ForeignKey -> drop-down list
    # slug = ...
    # upd_date = models.DateTimeField(auto_now=True)
    # is_published = models.BooleanField()

    def __str__(self):
        return f'{self.title}, {self.category}'
