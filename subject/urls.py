from django.conf.urls import url, include
from subject.views import SubjectListView, SubjectDetailView
from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    url(r'^$', SubjectListView.as_view(), name='subject-list'),
    url(r'^(?P<pk>\d+)/$', SubjectDetailView.as_view(), name='subject-detail'),
    ]