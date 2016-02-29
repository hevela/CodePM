# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'H.A.V.S'


def rootview(request):
    r_context = RequestContext(request, {})
    return render_to_response('index.html', r_context)