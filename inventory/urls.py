from django.conf.urls import url
from .views import *

##from django.contrib import admin

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^display_laptops$', display_laptops, name='display_laptops'),
    url(r'^display_desktop$', display_desktop, name='display_desktop'),
    url(r'^display_telefono$', display_telefono, name='display_telefono'),

    url(r'^add_laptop$', add_laptop, name='add_laptop'),
    url(r'^add_desktop$', add_desktop, name='add_desktop'),
    url(r'^add_telefono$', add_telefono, name='add_telefono'),



]
