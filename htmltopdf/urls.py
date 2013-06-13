from django.conf.urls import patterns, url

from htmltopdf import views

urlpatterns = patterns('',
    url(r'^$', views.upload, name='index'),
)
