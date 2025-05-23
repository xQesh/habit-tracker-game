from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(response):
    return render(response, 'tracker/home.html')