from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1> View de teste</h1>")

def contacts(request):
    return HttpResponse("<h1> Telefone: (21) 58656000</h1><p>Email: meuEmail@Gmail.com.br</p>")