from django.shortcuts import render, get_object_or_404, redirect
from .models import Biography, Article, InterestingRead, FamilyPhoto
from guestbook.models import GuestEntry
from django_ratelimit.decorators import ratelimit

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

def photos_ru(request):
    photos = FamilyPhoto.objects.all()
    return render(request, 'blog/ru/photos.html', {'photos': photos, 'lang_switch_url': '/en/photos/'})

def photos_en(request):
    photos = FamilyPhoto.objects.all()
    return render(request, 'blog/en/photos.html', {'photos': photos, 'lang_switch_url': '/ru/photos/'})

@ratelimit(key='ip', rate='3/h', method='POST', block=True)
def guestbook_ru(request):
    entries = GuestEntry.objects.using('guestbook').filter(approved=True, parent=None)
    error = None
    success = False

    if request.method == 'POST':
        if request.POST.get('honeypot'):
            return redirect('guestbook_ru')

        name = request.POST.get('name', '').strip()
        subject = request.POST.get('subject', '').strip()
        body = request.POST.get('body', '').strip()
        parent_id = request.POST.get('parent_id')

        if len(name) > 100:
            error = 'Имя слишком длинное. Пожалуйста, ограничьтесь 100 символами.'
        elif len(subject) > 200:
            error = 'Тема слишком длинная. Пожалуйста, ограничьтесь 200 символами.'
        elif not body or len(body) < 10:
            error = 'Пожалуйста, введите сообщение не менее 10 символов.'
        elif len(body) > 2000:
            error = 'Сообщение слишком длинное. Пожалуйста, ограничьтесь 2000 символами.'
        else:
            parent = None
            if parent_id:
                try:
                    parent = GuestEntry.objects.using('guestbook').get(id=parent_id)
                except GuestEntry.DoesNotExist:
                    pass
            GuestEntry.objects.using('guestbook').create(
                name=name, subject=subject, body=body, parent=parent
            )
            success = True

    return render(request, 'blog/ru/guestbook.html', {
        'entries': entries,
        'error': error,
        'success': success,
        'lang_switch_url': '/en/guestbook/',
    })


@ratelimit(key='ip', rate='3/h', method='POST', block=True)
def guestbook_en(request):
    entries = GuestEntry.objects.using('guestbook').filter(approved=True, parent=None)
    error = None
    success = False

    if request.method == 'POST':
        if request.POST.get('honeypot'):
            return redirect('guestbook_en')

        name = request.POST.get('name', '').strip()
        subject = request.POST.get('subject', '').strip()
        body = request.POST.get('body', '').strip()
        parent_id = request.POST.get('parent_id')

        if len(name) > 100:
            error = 'Name is too long. Please keep it under 100 characters.'
        elif len(subject) > 200:
            error = 'Subject is too long. Please keep it under 200 characters.'
        elif not body or len(body) < 10:
            error = 'Please enter a message of at least 10 characters.'
        elif len(body) > 2000:
            error = 'Message is too long. Please keep it under 2000 characters.'
        else:
            parent = None
            if parent_id:
                try:
                    parent = GuestEntry.objects.using('guestbook').get(id=parent_id)
                except GuestEntry.DoesNotExist:
                    pass
            GuestEntry.objects.using('guestbook').create(
                name=name, subject=subject, body=body, parent=parent
            )
            success = True

    return render(request, 'blog/en/guestbook.html', {
        'entries': entries,
        'error': error,
        'success': success,
        'lang_switch_url': '/ru/guestbook/',
    })

from django_ratelimit.exceptions import Ratelimited

def handler403(request, exception=None):
    if isinstance(exception, Ratelimited):
        return render(request, 'blog/en/guestbook.html', {
            'error': 'You have submitted too many messages. Please try again later.',
            'entries': GuestEntry.objects.using('guestbook').filter(approved=True, parent=None),
            'lang_switch_url': '/ru/guestbook/',
        }, status=429)
    return render(request, '403.html', status=403)