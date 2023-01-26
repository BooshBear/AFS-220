from django.shortcuts import render
from django.http import HttpResponse

def Browserpage(req):
    return render(req, 'Browserpage.html')