from django.shortcuts import render
import requests
from django.http import HttpResponse

def dictionary_definition(request,word):
    print(word)
    return HttpResponse(word)
