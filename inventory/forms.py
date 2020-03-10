from django import forms
from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = laptop
        fields = ('tipo', 'precio', 'estado', 'comentario')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('tipo', 'precio', 'estado', 'comentario')


class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ('tipo', 'precio', 'estado', 'comentario')
