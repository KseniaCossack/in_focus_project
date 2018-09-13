from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('somethin')

# Create your views here.
