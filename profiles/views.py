from django.shortcuts import render
from django.views.generic import DetailView
from users.models import Profile

class ProfileDetailView(DetailView):
    model = Profile
    slug_field = 'username'
    slug_url_kwarg = 'user_name'
