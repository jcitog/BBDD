from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('inicio', views.inicio, name='inicio'),
	path('quienes', views.quienes, name='quienes'),
	path('contacto', views.contacto, name='contacto'),
	path('evento', views.evento, name='evento'),
	path('preguntas', views.preguntas, name='preguntas'),
	path('pre', views.pre, name='pre'),
]