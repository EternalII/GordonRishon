from django.contrib import admin
from .models import Biography, Article, InterestingRead , VisitorCounter, FamilyPhoto

@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'date')
    search_fields = ('title_ru',)

@admin.register(InterestingRead)
class InterestingReadAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'author', 'date')
    search_fields = ('title_ru', 'author')

@admin.register(FamilyPhoto)
class FamilyPhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'order')