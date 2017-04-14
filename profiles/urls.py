from django.conf.urls import url, include
from profiles.views import ProfileDetailView
from django.conf.urls.i18n import urlpatterns

urlpatterns=[
    url(r'^(?P<user_name>.*)/$', ProfileDetailView.as_view(), name='profile_detail'),

    ]


