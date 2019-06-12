from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name ='music/index.html' 
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all() 

class DetailView(generic.DetailView):
    model =Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    success_url = reverse_lazy('music:index')



