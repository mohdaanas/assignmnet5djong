from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#should access Model objects and use Templates to prepare responses.
    return HttpResponse('Hello World')


