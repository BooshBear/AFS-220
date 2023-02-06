from django.shortcuts import render
from django.http import HttpResponse

def OrderPage(req):
    return render(req, 'orderPage.html')