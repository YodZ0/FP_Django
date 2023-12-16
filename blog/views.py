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


def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request=request,
                  template_name='article_page.html',
                  context=context,
                  )


def about_page(request):
    return render(request=request, template_name='about_page.html')


def contact_page(request):
    return render(request=request, template_name='contact_page.html')


# def categories_page(request):
#     articles = Article.objects.all()
#     articles = articles[::-1]
#     context = {'articles': articles}
#     return render(request=request,
#                   template_name='categories.html',
#                   context=context,
#                   )
