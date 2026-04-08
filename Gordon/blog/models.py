from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



class Biography(models.Model):
    content_ru = CKEditor5Field()
    content_en = CKEditor5Field(blank=True)
    image = models.ImageField(upload_to='biography/', null=True, blank=True)
    image_caption = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "My Biography"

    class Meta:
        verbose_name_plural = "Biography"


class Article(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    body_ru = models.TextField()
    body_en = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        ordering = ['-date']

class InterestingRead(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    body_ru = models.TextField()
    body_en = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        ordering = ['-date']