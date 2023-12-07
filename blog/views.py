from django.shortcuts import render
from blog.models import Article


# Create your views here.
def home_page(request):
    articles = Article.objects.all()
    articles = articles[::-1]
    context = {'articles': articles}
    return render(request=request,
                  template_name='home_page.html',
                  context=context,
                  )


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    return render(request=request,
                  template_name='article_page.html',
                  context=context,
                  )


def category_page(request):
    pass


# def categories_page(request):
#     articles = Article.objects.all()
#     articles = articles[::-1]
#     context = {'articles': articles}
#     return render(request=request,
#                   template_name='categories.html',
#                   context=context,
#                   )
