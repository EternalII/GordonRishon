from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_en, name='home_en'),
    path('biography/', views.biography_en, name='biography_en'),
    path('articles/', views.articles_en, name='articles_en'),
    path('articles/<int:pk>/', views.article_detail_en, name='article_detail_en'),
    path('interesting-reads/', views.interesting_reads_en, name='interesting_reads_en'),
]