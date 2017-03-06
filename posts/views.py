from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Posts
from subject.models import Subject
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template.context_processors import request
from django.shortcuts import get_object_or_404, render, redirect

class PostsDetailView(DetailView):
    model = Posts
    
def new_post(request):
    if request.method == "POST":
         return HttpResponse(request.POST['comment'])
        
    
        
