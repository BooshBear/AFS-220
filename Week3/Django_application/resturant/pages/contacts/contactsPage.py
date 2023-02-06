from django.shortcuts import render
from django.http import HttpResponse

def Contacts(req):
    return render(req, 'contactPage.html')