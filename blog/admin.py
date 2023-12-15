from django.contrib import admin
from blog.models import Article, Categories


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'pub_date']
    list_display_links = ['title']

    save_on_top = True


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass
