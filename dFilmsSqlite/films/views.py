from django.views import generic
from films.models import Acteur, Film
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'films/index.html'
    context_object_name = 'film_list'
    queryset = Film.objects.order_by('film_title')


# Film classes
class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'films/filmdetail.html'
    context_object_name = 'film'


class FilmCreateView(generic.CreateView):
    model = Film
    template_name = 'films/form.html'
    fields = ['acteurs', 'film_title']


class FilmUpdateView(generic.UpdateView):
    model = Film
    template_name = 'films/form.html'
    fields = ['acteurs', 'film_title']


class FilmDeleteView(generic.DeleteView):
    model = Film
    template_name = 'films/delete.html'
    success_url = reverse_lazy('films:index')


# Acteurs classes
class ActeurDetailView(generic.DetailView):
    model = Acteur
    template_name = 'films/acteurdetail.html'
    context_object_name = 'acteur'


class ActeurCreateView(generic.CreateView):
    model = Acteur
    template_name = 'films/form.html'
    fields = ['acteur_name']
