from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Hello</h1>')
