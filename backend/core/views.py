from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from .forms import RegistrationForm
from django.views.generic import CreateView

# Create your views here.

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


    


