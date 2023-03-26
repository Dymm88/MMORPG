from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .conf import CATEGORIES


class Person(models.Model):
    """Пользователи"""
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    """Объявления"""
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    header = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=2, choices=CATEGORIES)
    content = RichTextUploadingField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header


class Review(models.Model):
    """Отклики"""
    text = models.TextField(max_length=500)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
