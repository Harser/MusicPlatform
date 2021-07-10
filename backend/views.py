from django.views.generic import TemplateView
from django.views.generic import CreateView
from .models import Album, Track


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class AlbumCreateView(CreateView):
    model = Album
    template_name = 'album_form.html'
    fields = ('title', 'creator')


class TrackCreateView(CreateView):
    model = Track
    template_name = 'track_form.html'
    fields = ('title', 'lyrics', 'file')
