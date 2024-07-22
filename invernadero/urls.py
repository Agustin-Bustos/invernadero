from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import (
    InvernaderoListView,
    InvernaderoDetailView,
    InvernaderoCreateView,
    InvernaderoUpdateView,
    InvernaderoDeleteView,
    SensorListView,
    SensorDetailView,
    SensorCreateView,
    SensorUpdateView,
    SensorDeleteView
)

urlpatterns = [
    path('', InvernaderoListView.as_view(), name='invernadero_list'),
    path('<int:pk>/', InvernaderoDetailView.as_view(), name='invernadero_detail'),
    path('create/', InvernaderoCreateView.as_view(), name='invernadero_create'),
    path('update/<int:pk>/', InvernaderoUpdateView.as_view(), name='invernadero_update'),
    path('delete/<int:pk>/', InvernaderoDeleteView.as_view(), name='invernadero_delete'),
    path('sensors/', SensorListView.as_view(), name='sensor_list'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor_detail'),
    path('sensors/create/', SensorCreateView.as_view(), name='sensor_create'),
    path('sensors/update/<int:pk>/', SensorUpdateView.as_view(), name='sensor_update'),
    path('sensors/delete/<int:pk>/', SensorDeleteView.as_view(), name='sensor_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
