from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# views
def home(request):
    tmp = loader.get_template('home.html')
    return HttpResponse(tmp.render())