from django.shortcuts import render

from django.http import HttpResponse

from blog import views
def home(request):
    
    return views.post_list(request)

# Create your views here.
