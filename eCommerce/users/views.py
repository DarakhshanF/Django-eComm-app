from django.shortcuts import render
from .forms import RegistrationForm
from django.views import View
from django.contrib import messages

# Create your views here.
class registration(View):
    def get(self, request):
        return render(request, 'users/signup.html', {'form': RegistrationForm()})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User account created successfully! Please log in.")
            return render(request, 'users/signup.html', {'form': RegistrationForm()})
            # return HttpResponseRedirect(reverse_lazy('login'))  # Redirect to login page after successful signup
        return render(request, 'users/signup.html', {'form': form}) # displays any error messages, if any
