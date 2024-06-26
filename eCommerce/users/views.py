from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'users/homepage.html', context)

class registration(View):
    def get(self, request):
        return render(request, 'users/signup.html', {'form': RegistrationForm()})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User account created successfully! Please log in.")
            return redirect('users:login')
            # return render(request, 'users/signup.html', {'form': RegistrationForm()})
            # return HttpResponseRedirect(reverse_lazy('login'))  # Redirect to login page after successful signup
        else:
            return render(request, 'users/signup.html', {'form': form})
        return render(request, 'users/signup.html', {'form': form}) # displays any error messages, if any

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('users:home')
            else:
                form.add_error(None, 'Username or password is incorrect. Please try again')
        return render(request, 'users/login.html', {'form': form}) # display error messages
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('users:login')