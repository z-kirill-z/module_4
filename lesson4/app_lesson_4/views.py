from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return HttpResponse('Домашка по 4 занятию')