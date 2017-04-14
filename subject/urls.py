from django.conf.urls import url, include
from subject.views import SubjectListView, SubjectDetailView
from posts.views import PostsDetailView
from django.conf.urls.i18n import urlpatterns
from . import views

urlpatterns = [
    url(r'^$', SubjectListView.as_view(), name='subject-list'),
    url(r'^(?P<pk>\d+)/$', SubjectDetailView.as_view(), name='subject-detail'),
    url(r'^newSubject/$', views.subjectNew, name='subject-new'),
    ]