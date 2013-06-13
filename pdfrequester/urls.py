from django.conf.urls import patterns, url

from pdfrequester import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^download/$', views.download, name='download'),
    url(r'^upload/download/$', views.download, name='download'),
    url(r'^upload/$', views.upload, name='upload'),
)
