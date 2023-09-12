from django.shortcuts import render
from .models import Project

def home(req):
    projects = Project.objects.all()
    return render(req, 'home.html', {'proyects': projects})