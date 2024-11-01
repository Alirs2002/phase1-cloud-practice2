from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.core.cache import cache

def dictionary_definition(request,word):

    cached_data = cache.get(word)

    if(cached_data):
        return(HttpResponse(f"response is from cache: {cached_data}"))



    api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': 'UQNmRzC9t1DfaansEEfz1Q==04WUlN7tuwStTX9f'})

    if response.status_code == requests.codes.ok:
        cache.set(word,response.text,timeout=300)
        return HttpResponse(f"response is from API: {response.text}")
    else:
        print("Error:", response.status_code, response.text)




def randomword(request):

    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': 'UQNmRzC9t1DfaansEEfz1Q==04WUlN7tuwStTX9f'})
    if response.status_code == requests.codes.ok:
        return HttpResponse(response.text)
    else:
        print("Error:", response.status_code, response.text)
