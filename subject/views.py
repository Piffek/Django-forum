from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Subject
from posts.models import Posts
from django.http import HttpResponse
from django.template.context_processors import request
from pip._vendor.requests.models import Request
from .forms import SubjectForm
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, render, redirect

class SubjectListView(ListView):
    model = Subject
    
class SubjectDetailView(DetailView):
    model = Subject
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_obj'] = Posts.objects.filter(subj=self.kwargs['pk']).order_by('-when')
        return context
    
def subjectNew(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.who = request.user
            post.save()
            return redirect('/')
    else:
        form = SubjectForm()
    return render(request, 'subject/new_subject.html', {'form': form})



