from django.conf.urls import patterns, include, url
from userprofile import views
urlpatterns = patterns('',
        url(r'', views.user_profile),
)