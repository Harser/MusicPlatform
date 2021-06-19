from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=1023)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Track(models.Model):
    title = models.CharField(max_length=511)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    lyrics = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/tracks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



