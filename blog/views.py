from django.shortcuts import render
from blog.models import Article


# Create your views here.
def home_page(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request=request,
                  template_name='home_page.html',
                  context=context,
                  )
