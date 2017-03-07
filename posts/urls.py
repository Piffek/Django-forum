from django.conf.urls import url, include
from subject.views import SubjectListView, SubjectDetailView
from posts.views import PostsDetailView
from django.conf.urls.i18n import urlpatterns
from . import views


urlpatterns = [
    url(r'^new_post/$', views.new_post, name='new_post'),
    ]