from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    return HttpResponse('home 1')
    # return HTTP Response


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')