from django.shortcuts import render, get_object_or_404
from .models import Biography, Article, InterestingRead

def landing(request):
    return render(request, 'landing.html')

def home_ru(request):
    return render(request, 'blog/ru/home.html', {'lang_switch_url': '/en/'})

def home_en(request):
    return render(request, 'blog/en/home.html', {'lang_switch_url': '/ru/'})

def biography_ru(request):
    bio = Biography.objects.first()
    return render(request, 'blog/ru/biography.html', {'bio': bio, 'lang_switch_url': '/en/biography/'})

def biography_en(request):
    bio = Biography.objects.first()
    return render(request, 'blog/en/biography.html', {'bio': bio, 'lang_switch_url': '/ru/biography/'})

def articles_ru(request):
    articles = Article.objects.all()
    return render(request, 'blog/ru/articles.html', {'articles': articles, 'lang_switch_url': '/en/articles/'})

def articles_en(request):
    articles = Article.objects.all()
    return render(request, 'blog/en/articles.html', {'articles': articles, 'lang_switch_url': '/ru/articles/'})

def article_detail_ru(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/ru/article_detail.html', {'article': article, 'lang_switch_url': f'/en/articles/{pk}/'})

def article_detail_en(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/en/article_detail.html', {'article': article, 'lang_switch_url': f'/ru/articles/{pk}/'})

def interesting_reads_ru(request):
    reads = InterestingRead.objects.all()
    return render(request, 'blog/ru/interesting_reads.html', {'reads': reads, 'lang_switch_url': '/en/interesting-reads/'})

def interesting_reads_en(request):
    reads = InterestingRead.objects.all()
    return render(request, 'blog/en/interesting_reads.html', {'reads': reads, 'lang_switch_url': '/ru/interesting-reads/'})

def family_tree_en(request):
    return render(request, 'blog/en/family_tree.html', {'lang_switch_url': '/ru/family-tree/'})

def family_tree_ru(request):
    return render(request, 'blog/ru/family_tree.html', {'lang_switch_url': '/en/family-tree/'})