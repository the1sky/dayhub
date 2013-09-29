from django.conf.urls import patterns,include,url
from views import hello,homepage, current_datetime, hours_ahead,mysql

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^./', include('foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    ( r'^hello/$', hello ),
    ( r'^$', homepage ),
    ( r'^time/$', current_datetime ),
    ( r'^time/plus/(\d{1,2})/$', hours_ahead ),
    ( r'^mysql/$', mysql ),
    )