from django.db import models

# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    songname = models.CharField(max_length=50, default="")
    artist = models.CharField(max_length=50, default="")
    img = models.ImageField(upload_to="mplayer/static", null=True, blank=True)
    audio = models.FileField(upload_to="mplayer/static/audio", max_length=254, null=True)

    def __str__(self):
        return self.songname