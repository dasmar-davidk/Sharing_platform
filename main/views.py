from django.shortcuts import render, redirect
from django.contrib.auth.models import UserCreationForm
from .forms import CompanyProfile, ProjectForm
from .models import CompanyProfile, Project

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_vaild():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            return redirect(request, 'registration/register.html', {'form' : form})

def create_company_profile(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST)
        if form.is_vaild():
            form.save()
            company_profile = form.save(comit=False)
            company_profile.user = request.user
            company_profile.user()
            return redirect('home')
        else:
            form = CompanyProfileForm(request.POST)
            return redirect(request, 'create_company_profile', {'form' : form})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_vaild():
            form.save()
            project = form.save(comit=False)
            project.company = request.user.companyprofile
            project.save()
            return redirect('project_detail', pk=project.pk)
        else:
            form = ProjectForm
            return redirect(request, 'create_project', {'form' : form})