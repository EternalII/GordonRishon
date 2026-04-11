import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

import argostranslate.package
import argostranslate.translate
from blog.models import Article

# Download and install the Russian → English language package (first time only)
print("Setting up translation package...")
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package = next(
    filter(lambda x: x.from_code == "ru" and x.to_code == "en", available_packages)
)
argostranslate.package.install_from_path(package.download())
print("Package ready!")

# Translate
articles = Article.objects.filter(body_en='', title_en='')
total = articles.count()
print(f"Translating {total} articles...")

for i, article in enumerate(articles, 1):
    try:
        article.title_en = argostranslate.translate.translate(article.title_ru, "ru", "en")
        article.body_en  = argostranslate.translate.translate(article.body_ru,  "ru", "en")
        article.save()
        print(f"[{i}/{total}] Translated: {article.title_ru}")
    except Exception as e:
        print(f"[{i}/{total}] Failed: {article.title_ru} — {e}")

print("Done!")