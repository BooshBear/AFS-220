from django.shortcuts import render, redirect
from django.contrib.auth import logout

from meal.models import Category, Meal

from .forms import SignupForm

# Create your views here.

def index(request):
    category = request.GET.get('category')
    
    if category == None:
        meals = Meal.objects.all()
    else:
        meals = Meal.objects.filter(category__name=category)
    
    categories = Category.objects.all()
    return render(request, 'core/browser.html', {
        'categories': categories,
        'meals': meals,
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
    
def logout_req(request):
    logout(request)
    return redirect("/")