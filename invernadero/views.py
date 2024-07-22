from django.urls import reverse_lazy
from .models import Invernadero, Sensor
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class InvernaderoListView(ListView):
    model = Invernadero
    template_name = 'invernadero/invernadero_list.html'

class InvernaderoDetailView(DetailView):
    model = Invernadero
    template_name = 'invernadero/invernadero_detail.html'

class InvernaderoCreateView(CreateView):
    model = Invernadero
    fields = ['nombre', 'ubicacion', 'usuario']
    template_name = 'invernadero/invernadero_form.html'
    success_url = reverse_lazy('invernadero_list')

class InvernaderoUpdateView(UpdateView):
    model = Invernadero
    fields = ['nombre', 'ubicacion', 'usuario']
    template_name = 'invernadero/invernadero_form.html'
    success_url = reverse_lazy('invernadero_list')

class InvernaderoDeleteView(DeleteView):
    model = Invernadero
    template_name = 'invernadero/invernadero_confirm_delete.html'
    success_url = reverse_lazy('invernadero_list')

class SensorListView(ListView):
    model = Sensor
    template_name = 'invernadero/sensor_list.html'

class SensorDetailView(DetailView):
    model = Sensor
    template_name = 'invernadero/sensor_detail.html'

class SensorCreateView(CreateView):
    model = Sensor
    fields = ['nombre', 'ubicacion', 'usuario']
    template_name = 'invernadero/sensor_form.html'
    success_url = reverse_lazy('sensor_list')

class SensorUpdateView(UpdateView):
    model = Sensor
    fields = ['nombre', 'ubicacion', 'usuario']
    template_name = 'invernadero/sensor_form.html'
    success_url = reverse_lazy('sensor_list')

class SensorDeleteView(DeleteView):
    model = Sensor
    template_name = 'invernadero/sensor_confirm_delete.html'
    success_url = reverse_lazy('sensor_list')
