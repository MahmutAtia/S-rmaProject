from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from .forms import RegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
# Create your views here.

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def get_context_data(self) :
        context = super().get_context_data()
        context["obj"] = "hey i can do it"
        return context
    

    

class Login(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = False
    
    def get_context_data(self) :
        context = super().get_context_data()
        context["obj"] = "hey i can do it"
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy("home")
    def form_invalid(self, form) :
        messages.error(self.request, "invalild")
        return self.render_to_response(self.get_context_data(form=form))

    


