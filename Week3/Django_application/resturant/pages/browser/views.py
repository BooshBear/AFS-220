from django.shortcuts import render

def Browserpage(req):
    return render(req, 'Browserpage.html')