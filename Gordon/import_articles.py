import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from docx import Document
from blog.models import Article

ARTICLES_FOLDER = 'articles'  # folder where your .docx files live

for filename in os.listdir(ARTICLES_FOLDER):
    if not filename.endswith('.docx'):
        continue

    path = os.path.join(ARTICLES_FOLDER, filename)
    doc = Document(path)

    # Use the filename (without extension) as the title
    title = os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' ').title()

    # Join all paragraphs as the body
    body = '\n\n'.join(p.text for p in doc.paragraphs if p.text.strip())

    # Skip if already imported
    if Article.objects.filter(title=title).exists():
        print(f'Skipping (already exists): {title}')
        continue

    Article.objects.create(title=title, body=body)
    print(f'Imported: {title}')

print('Done!')