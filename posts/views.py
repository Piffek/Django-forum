from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Posts
from subject.models import Subject
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template.context_processors import request
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

class PostsDetailView(DetailView):
    model = Posts

def new_post(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            newpost = Posts(text=request.POST['comment'], subj_id=request.POST['subj_id'], who_id=request.user.id)
            newpost.save()
            return redirect('/')
         
        
    
        
