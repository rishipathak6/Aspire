from django.shortcuts import render
from django.core import serializers

from landpage.models import CoursePreview
from registrar.models import Course

import json
from django.http import HttpResponse
from django.conf import settings


def landpage_page(request):
    return render(request, 'landpage/main/index.html',{
        'local_css_urls' : settings.AGENCY_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.AGENCY_JS_LIBRARY_URLS
    })


def course_preview_modal(request):
    course = None
    if request.method == u'POST':
        POST = request.POST
        course_id = POST.get('course_id')
        if course_id is not None:
            try:
                course = Course.objects.get(id=int(course_id))
            except Course.DoesNotExist:
                pass
    return render(request, 'landpage/main/course_preview.html',{
        'course' : course
    })

