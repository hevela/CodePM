import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from projects.models import Project
from python_recipes import get_week_of_month_from_datetime, \
    get_week_start_datetime_end_datetime_tuple
from tracking.models import Tracking


class WeekTracking(LoginRequiredMixin, ListView):
    model = Tracking
    login_url = '/login/'

    def get_queryset(self):
        today = self.request.GET.get('today', None)
        if today is None:
            today = datetime.datetime.today()
        this_week = get_week_of_month_from_datetime(today)
        week_start = get_week_start_datetime_end_datetime_tuple(
            today.year, today.month, this_week)[0]
        week = []
        projects = Project.objects.filter(
            proj_participants__team_member=self.request.user).values('name')
        projects = list(projects)
        for i in range(0, 5):
            week.append(dict(
                day=week_start + datetime.timedelta(days=i),
                projects=projects
            ))
        return week