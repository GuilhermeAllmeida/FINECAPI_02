from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from reserva.models import Reserva

class ReservaList(ListView):
    model = Reserva
    queryset = Reserva.objects.all()
    

class ReservaCreate(CreateView):
    model = Reserva
    fields = '__all__'
    success_url = reverse_lazy('reserva:list')
    success_message = "Reserva criada com sucesso!"

class ReservaUpdate(UpdateView):
    model = Reserva
    fields = '__all__'
    success_url = reverse_lazy('reserva:list')

class ReservaDetail(DetailView):
    queryset = Reserva.objects.all()

class ReservaDelete(DeleteView):
    model = Reserva
    queryset = Reserva.objects.all()
    success_url = reverse_lazy('reserva:list')