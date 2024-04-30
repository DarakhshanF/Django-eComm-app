from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about-us.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the form data to the database
            messages.success(request, "The Contact form has been submitted successfully.")
            return redirect('home:contact')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})
