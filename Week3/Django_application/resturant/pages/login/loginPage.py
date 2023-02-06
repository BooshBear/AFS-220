from django.shortcuts import render
from django.http import HttpResponse

def LoginPage(req):
    return render(req, 'loginPage.html')