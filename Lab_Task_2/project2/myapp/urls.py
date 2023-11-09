# Author : Usama Tahir
# Created on : Nov 9 2023
# Matriculation number : 1453517


from django.urls import path
from . import views

urlpatterns = [
    path('api/data/', views.api_data, name='api_data'),
]
