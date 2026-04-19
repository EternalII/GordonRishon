from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



class Biography(models.Model):
    content_ru = CKEditor5Field(config_name='default')
    content_en = CKEditor5Field(blank=True, config_name='default')
    image = models.ImageField(upload_to='biography/', null=True, blank=True)
    image_caption = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "My Biography"

    class Meta:
        verbose_name_plural = "Biography"


class Article(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    body_ru = CKEditor5Field(config_name='default')
    body_en = CKEditor5Field(blank=True, config_name='default')
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    image_position = models.CharField(max_length=10, choices=[
        ('top', 'Top'),
        ('bottom', 'Bottom'),
    ], default='top', blank=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        ordering = ['title_ru']

class InterestingRead(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    body_ru = CKEditor5Field(config_name='default', default='')
    body_en = CKEditor5Field(blank=True, config_name='default')
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        ordering = ['-date']

class FamilyPhoto(models.Model):
    image = models.ImageField(upload_to='family/')
    caption_ru = models.CharField(max_length=300, blank=True)
    caption_en = models.CharField(max_length=300, blank=True)
    date = models.DateField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.caption_ru or f"Photo {self.id}"

    class Meta:
        ordering = ['order']

class VisitorCounter(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Visitors: {self.count}"