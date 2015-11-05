"""eksi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from eksiapp.views import  (  all_titles, title, submit_entry)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^titles/', all_titles, name = 'title-json'),
    url(r'^title/(?P<title_id>[0-9]+)/$', title, name = 'entry-json'),
    url(r'^submit_entry/', submit_entry, name='submit-entry'),
]
