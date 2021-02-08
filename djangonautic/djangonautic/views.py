#here we will create the functions to fire the page decided by the url router
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')


def about(request):
    #for now just sending back a simple http response
    # return HttpResponse('about')
    return render(request, 'about.html')
