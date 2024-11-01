
from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('dictionary/<str:word>/', views.dictionary_definition, name='dictionary_definition'),
    path('randomword/', views.randomword, name='dictionary_definition'),

]
