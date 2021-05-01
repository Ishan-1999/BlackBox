from django.shortcuts import render
from .models import Song
import json

# Create your views here.
def index(request):
    songs = Song.objects.all()
    Allsongs = []
    for item in songs:
        Allsongs.append({'songname': item.songname, 'artist': item.artist, 'img': item.img,  'audio': item.audio})
        response = json.dumps(Allsongs, default=str)
    return render(request, 'musicplayer.html', {'data': response, 'songs': songs})