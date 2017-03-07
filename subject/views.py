from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Subject
from posts.models import Posts
from django.http import HttpResponse
from django.template.context_processors import request
from pip._vendor.requests.models import Request

class SubjectListView(ListView):
    model = Subject
    
class SubjectDetailView(DetailView):
    model = Subject
    
    def get_context_data(self, **kwargs):
        context = super(SubjectDetailView, self).get_context_data(**kwargs)
        context['posts_obj'] = Posts.objects.filter(subj=self.kwargs['pk']).order_by('-when')
        return context


