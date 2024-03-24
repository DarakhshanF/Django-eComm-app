from django.shortcuts import render
from .forms import RegisterationForm
from django.views import View
from django.contrib import messages

# Create your views here.
class registeration(View):
    def get(self, request):
        return render(request, 'users/signup.html', {'form': RegisterationForm()})

    def post(self, request):
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User account created successfully! Please log in.")
            return render(request, 'users/signup.html', {'form': RegisterationForm()})
            # return HttpResponseRedirect(reverse_lazy('login'))  # Redirect to login page after successful signup
        return render(request, 'users/signup.html', {'form': form}) # displays any error messages, if any
