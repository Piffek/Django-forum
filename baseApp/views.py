from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'
    
index_page = HomePageView.as_view()
