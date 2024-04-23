from django.db import models
from django.contrib.auth.models import User

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Project(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)