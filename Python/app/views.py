from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse(
        '<h1> Hello word do CRUD</h1>'

    )

def login(request):
    return HttpResponse(

        'Tela de Login'


    )