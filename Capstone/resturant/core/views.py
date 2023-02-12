from django.shortcuts import render, redirect

from meal.models import Category, Meal

from .forms import SignupForm

# Create your views here.

def index(request):
    meals = Meal.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/browser.html', {
        'categories': categories,
        'items': meals,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form,
    })