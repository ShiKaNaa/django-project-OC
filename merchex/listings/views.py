# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listing</h1> <p>Nous adorons merch !</p>')

def contact_us(request):
    return HttpResponse('<h1>Nous contacter</h1> <p>Nous adorons merch !</p>')
