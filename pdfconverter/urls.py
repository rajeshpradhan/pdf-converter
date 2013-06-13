from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdfconverter.views.home', name='home'),
    # url(r'^pdfconverter/', include('pdfconverter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
   url(r'^pdfrequester/', include('pdfrequester.urls')),
   url(r'^htmltopdf/', include('htmltopdf.urls')),
   url(r'^pdfrequester/htmltopdf/', include('htmltopdf.urls')),
   url(r'^pdfrequester/upload/upload/', include('htmltopdf.urls')),
)
