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
    lyrics = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/tracks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TrackAlbum(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    previous = models.ForeignKey('self', on_delete=models.CASCADE, related_name='next', blank=True,
                                 null=True)
