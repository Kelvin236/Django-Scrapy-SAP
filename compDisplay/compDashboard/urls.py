# File:    urls.py
# Author:  Kelvin Lawson
# Date:    May 5, 2018
# Version: 1.0
#
# Purpose: To match a view function to paricular url. This allows a webpage's
#          content to be viewed when it is requested.

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-prof-info', views.get_prof_info_api, name='get_prof_info'),
    path('get-sup-staff-info', views.get_sup_staff_info_api, name='get_sup_staff_info'),
    path('get-events-info', views.get_events_info_api, name='get_events_info'),
]
