from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<slug:slug>', views.article_page),
    # path('about/', views.about_page),
    # path('categories/', views.categories_page),
    # path('category/', views.category_page),
    # path('contact/', views.contact_page),
]
