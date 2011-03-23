from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': '/home/toddj/Envs/djtest/Chillispot-Radius-Administration-Webapp/static'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': '/home/toddj/Envs/djtest/Chillispot-Radius-Administration-Webapp/media'}),
    (r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/', include(admin.site.urls)),
)
