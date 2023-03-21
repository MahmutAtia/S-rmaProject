from django.shortcuts import render
from django.views.generic import ListView
from .models import Company


class CompaniesListView(ListView):
    model = Company
    queryset = Company.objects.all()
    template_name= "core/index.html"

    def get_context_data(self) :
        context = super().get_context_data()
        context["obj"] = "my name is mamp"
             
        return context

