from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'landingapp.views.A1V1_landing', name='A1V1_landing_url'),
    url(r'^contactus/$', 'contactus.views.A2V1_contactus', name='contactus_url'),
    # url(r'^krunksystems/', include('krunksystems.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
