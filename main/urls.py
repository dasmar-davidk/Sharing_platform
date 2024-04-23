from django.urls import path
from .views import register, create_company_profile, create_project

urlpatterns = [
    path('register/', name=register),
    path('create_company_profile', name=create_company_profile),
    path('create_project', name=create_project),
]