from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    # path('<str:category>/<slug:slug>', views.article_page, name='article_page'),
    path('category/<slug:slug>', views.article_page, name='article_page'),
    path('about/', views.about_page),
    path('contact/', views.contact_page),
    # path('categories/', views.categories_page),
    # path('<str:category>/', views.category_page),
]
