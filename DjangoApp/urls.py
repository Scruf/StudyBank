"""
Definition of urls for DjangoApp.
"""

from datetime import datetime
from django.conf.urls import url
from app.forms import BootstrapAuthenticationForm
from app.views import *
from app.models import *
from django.contrib.auth.views import *


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
     

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
