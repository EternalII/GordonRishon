from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_ru, name='home_ru'),
    path('biography/', views.biography_ru, name='biography_ru'),
    path('articles/', views.articles_ru, name='articles_ru'),
    path('articles/<int:pk>/', views.article_detail_ru, name='article_detail_ru'),
    path('interesting-reads/', views.interesting_reads_ru, name='interesting_reads_ru'),
    path('interesting-reads/<int:pk>/', views.interesting_reads_detail_ru, name='interesting_reads_detail_ru'),
    path('family-tree/', views.family_tree_ru, name='family_tree_ru'),
    path('photos/', views.photos_ru, name='photos_ru'),
    path('guestbook/', views.guestbook_ru, name='guestbook_ru'),
]