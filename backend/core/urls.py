from django.urls import path
from companies.views import CompaniesListView
from .views import RegistrationView
urlpatterns = [
    path('', CompaniesListView.as_view()), 
    path('signup/', RegistrationView.as_view())
]