# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from .forms import *


from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_laptops(request):
    items = laptop.objects.all()
    context = {
        'items': items,
        'header': 'laptop',
    }
    return render(request, 'index.html', context)


def display_telefono(request):
    items = Telefono.objects.all()
    context = {
        'items': items,
        'header': 'Telefono',
    }
    return render(request, 'index.html', context)


def display_desktop(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktop',
    }
    return render(request, 'index.html', context)


def add_dispositivo(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = LaptopForm()
        return render(request, 'add_new.html', {'form': form})


def add_laptop(request):
    return add_dispositivo(request, LaptopForm)


def add_desktop(request):
    return add_dispositivo(request, DesktopForm)


def add_telefono(request):
    return add_dispositivo(request, TelefonoForm)


# def desplegar_cuotas(request):
