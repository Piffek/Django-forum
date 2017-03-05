from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Subject

class SubjectListView(ListView):
    model = Subject
    
class SubjectDetailView(DetailView):
    model = Subject

