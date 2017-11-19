#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text="<h1> Welcome to my app</h1>"
    return HttpResponse(text)
def Grocery_List(request):
    return HttpResponse("Here are a list of items: ")
