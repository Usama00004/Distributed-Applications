from django.shortcuts import render
import requests
from django.http import JsonResponse

def api_data(request):
    api_url = 'https://randomuser.me/api/'
    response = requests.get(api_url)
    data = response.json()
    return JsonResponse(data, safe=False)

