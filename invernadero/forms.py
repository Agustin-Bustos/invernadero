from django import forms
from .models import *

class Invernadero_form(forms.ModelForm):
    class Meta:
        model = Invernadero
        fields = ("__all__")
        
class Sensor_form(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ("__all__")

