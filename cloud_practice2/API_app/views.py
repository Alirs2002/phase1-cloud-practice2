from django.shortcuts import render
import requests
from django.http import HttpResponse

def dictionary_definition(request,word):
    print(word)

    api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': 'UQNmRzC9t1DfaansEEfz1Q==04WUlN7tuwStTX9f'})
    if response.status_code == requests.codes.ok:
        return HttpResponse(response.text)
    else:
        print("Error:", response.status_code, response.text)




def randomword(request):

    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': 'UQNmRzC9t1DfaansEEfz1Q==04WUlN7tuwStTX9f'})
    if response.status_code == requests.codes.ok:
        return HttpResponse(response.text)
    else:
        print("Error:", response.status_code, response.text)
