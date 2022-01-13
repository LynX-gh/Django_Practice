from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Make, Auto

# Create your views here.

class AutoIndex(LoginRequiredMixin, generic.ListView):
    template_name = 'autos/index.html'
    model = Auto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['make_count'] = Make.objects.all().count()
        return context

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:index')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:index')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = reverse_lazy('autos:index')

class MakeList(LoginRequiredMixin, generic.ListView):
    template_name = 'autos/make_list.html'
    model = Make

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:index')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:index')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    success_url = reverse_lazy('autos:index')