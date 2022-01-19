from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Breed, Cat

# Create your views here.

class CatIndex(LoginRequiredMixin, generic.ListView):
    template_name = 'cats/index.html'
    model = Cat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breed_count'] = Breed.objects.all().count()
        return context

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:index')

class BreedList(LoginRequiredMixin, generic.ListView):
    template_name = 'cats/breed_list.html'
    model = Breed

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:index')