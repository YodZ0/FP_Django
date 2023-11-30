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
