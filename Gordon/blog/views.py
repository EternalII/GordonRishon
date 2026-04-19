from django.shortcuts import render, get_object_or_404, redirect
from .models import Biography, Article, InterestingRead, FamilyPhoto
from guestbook.models import GuestEntry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def _get_guestbook_page(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)
    page = request.GET.get('page')
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)


def _process_guestbook_form(request, messages):
    name = request.POST.get('name', '').strip()
    subject = request.POST.get('subject', '').strip()
    body = request.POST.get('body', '').strip()
    parent_id = request.POST.get('parent_id')

    if len(name) > 100:
        return messages['name_len'], False
    elif len(subject) > 200:
        return messages['subject_len'], False
    elif not body or len(body) < 10:
        return messages['body_short'], False
    elif len(body) > 2000:
        return messages['body_long'], False

    parent = None
    if parent_id:
        try:
            parent = GuestEntry.objects.using('guestbook').get(id=parent_id)
        except GuestEntry.DoesNotExist:
            pass

    GuestEntry.objects.using('guestbook').create(
        name=name, subject=subject, body=body, parent=parent
    )
    return None, True


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

def interesting_reads_detail_en(request, pk):
    read = get_object_or_404(InterestingRead, pk=pk)
    return render(request, 'blog/en/interesting_reads_detail.html', {'read': read, 'lang_switch_url': f'/ru/interesting-reads/{pk}/'})

def interesting_reads_detail_ru(request, pk):
    read = get_object_or_404(InterestingRead, pk=pk)
    return render(request, 'blog/ru/interesting_reads_detail.html', {'read': read, 'lang_switch_url': f'/en/interesting-reads/{pk}/'})

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

def guestbook_ru(request):
    entries = GuestEntry.objects.using('guestbook').filter(approved=True, parent=None).order_by('-date')
    error = None
    success = False

    if request.method == 'POST' and request.POST.get('honeypot'):
        return redirect('guestbook_ru')

    if request.method == 'POST':
        error, success = _process_guestbook_form(request, {
            'name_len': 'Имя слишком длинное. Пожалуйста, ограничьтесь 100 символами.',
            'subject_len': 'Тема слишком длинная. Пожалуйста, ограничьтесь 200 символами.',
            'body_short': 'Пожалуйста, введите сообщение не менее 10 символов.',
            'body_long': 'Сообщение слишком длинное. Пожалуйста, ограничьтесь 2000 символами.',
        })

    page_entries = _get_guestbook_page(request, entries)

    return render(request, 'blog/ru/guestbook.html', {
        'entries': page_entries,
        'page_obj': page_entries,
        'error': error,
        'success': success,
        'lang_switch_url': '/en/guestbook/',
    })


def guestbook_en(request):
    entries = GuestEntry.objects.using('guestbook').filter(approved=True, parent=None).order_by('-date')
    error = None
    success = False

    if request.method == 'POST' and request.POST.get('honeypot'):
        return redirect('guestbook_en')

    if request.method == 'POST':
        error, success = _process_guestbook_form(request, {
            'name_len': 'Name is too long. Please keep it under 100 characters.',
            'subject_len': 'Subject is too long. Please keep it under 200 characters.',
            'body_short': 'Please enter a message of at least 10 characters.',
            'body_long': 'Message is too long. Please keep it under 2000 characters.',
        })

    page_entries = _get_guestbook_page(request, entries)

    return render(request, 'blog/en/guestbook.html', {
        'entries': page_entries,
        'page_obj': page_entries,
        'error': error,
        'success': success,
        'lang_switch_url': '/ru/guestbook/',
    })