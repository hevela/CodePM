from django.contrib import admin

from projects.models import Participant, Project, Iteration, Feature, \
    StatusFeature

admin.site.register(Project)
admin.site.register(Participant)
admin.site.register(Iteration)
admin.site.register(Feature)
admin.site.register(StatusFeature)
