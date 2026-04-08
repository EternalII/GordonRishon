from django.shortcuts import render, get_object_or_404
from .models import Biography, Article, InterestingRead

# Russian Views

def home_ru(request):
    recent_articles = Article.objects.all()[:3]
    recent_reads = InterestingRead.objects.all()[:3]
    return render(request, 'blog/ru/home.html', {
        'recent_articles': recent_articles,
        'recent_reads': recent_reads,
    })

def biography_ru(request):
    bio = Biography.objects.first()
    return render(request, 'blog/ru/biography.html', {'bio': bio})

def articles_ru(request):
    articles = Article.objects.all()
    return render(request, 'blog/ru/articles.html', {'articles': articles})

def article_detail_ru(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/ru/article_detail.html', {'article': article})

def interesting_reads_ru(request):
    reads = InterestingRead.objects.all()
    return render(request, 'blog/ru/interesting_reads.html', {'reads': reads})

# English views

def home_en(request):
    recent_articles = Article.objects.all()[:3]
    recent_reads = InterestingRead.objects.all()[:3]
    return render(request, 'blog/en/home.html', {
        'recent_articles': recent_articles,
        'recent_reads': recent_reads,
    })

def biography_en(request):
    bio = Biography.objects.first()
    return render(request, 'blog/en/biography.html', {'bio': bio})

def articles_en(request):
    articles = Article.objects.all()
    return render(request, 'blog/en/articles.html', {'articles': articles})

def article_detail_en(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/en/article_detail.html', {'article': article})

def interesting_reads_en(request):
    reads = InterestingRead.objects.all()
    return render(request, 'blog/en/interesting_reads.html', {'reads': reads})