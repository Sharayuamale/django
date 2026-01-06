from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    st="<h1>Welcome to our First Application</h1>"
    return HttpResponse(st)