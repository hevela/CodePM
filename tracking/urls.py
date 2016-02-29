# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import WeekTracking
__author__ = 'H.A.V.S'


urlpatterns = [
    url(r'^week/$', WeekTracking.as_view(), name='tracking_week'),
]