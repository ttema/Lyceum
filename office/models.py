from django.contrib.auth import admin
from django.db import models
from django.conf import settings
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200, default='')
    prev = models.TextField(blank=True, max_length=200, default='')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(blank=True, upload_to='articles_images', default=None)

    def create_preview(self):
        if self.prev == '':
            self.prev = self.text[:100] + '...'

    def __str__(self):
        return self.title


class TimePeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Album(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField(blank=True, max_length=200, default='')


class Photo(models.Model):
    photo = models.ImageField(blank=True, upload_to='gallery', default=None)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
