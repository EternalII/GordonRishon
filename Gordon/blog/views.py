from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Biography, Article, InterestingRead

def home(request):
    recent_articles = Article.objects.all()[:3]
    recent_reads = InterestingRead.objects.all()[:3]
    return render(request, 'blog/home.html', {
        'recent_articles': recent_articles,
        'recent_reads': recent_reads,
    })

def biography(request):
    bio = Biography.objects.first()
    return render(request, 'blog/biography.html', {'bio': bio})

def articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

def interesting_reads(request):
    reads = InterestingRead.objects.all()
    return render(request, 'blog/interesting_reads.html', {'reads': reads})