from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Subject
from django.http import HttpResponse
from django.template.context_processors import request
from pip._vendor.requests.models import Request

class SubjectListView(ListView):
    model = Subject
    
class SubjectDetailView(DetailView):
    model = Subject


