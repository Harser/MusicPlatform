from django.views.generic import TemplateView, CreateView

from .forms import AlbumForm, TrackForm
from .models import Album, Track


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = '/'


class TrackCreateView(CreateView):
    model = Track
    form_class = TrackForm
    template_name = 'track_form.html'
    success_url = '/'
