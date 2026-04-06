from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('biography/', views.biography, name='biography'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('interesting-reads/', views.interesting_reads, name='interesting_reads'),
]

'''
Check out the tutorial for more details:
https://docs.djangoproject.com/en/6.0/intro/tutorial03/
'''