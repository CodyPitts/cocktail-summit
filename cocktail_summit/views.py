from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import datetime
from datetime import timedelta
from .models import Speaker, Sponsor, Session
from bakery.views import BuildableListView, BuildableTemplateView

class SpeakersView(BuildableListView):
    model = Speaker
    template_name = 'cocktail_summit/speakers.html'
    context_object_name = 'speaker_list'
    build_path = 'speakers/index.html'
    queryset = Speaker.objects.all()

class SponsorsView(BuildableListView):
    model = Sponsor
    template_name = 'cocktail_summit/sponsors.html'
    context_object_name = 'sponsor_list'
    build_path = 'sponsors/index.html'

    def get_sponsors(self):
        return Sponsor.objects

class SessionsView(BuildableListView):
    model = Session
    template_name = 'cocktail_summit/schedule.html'
    context_object_name = 'session_list'
    build_path = 'sessions/index.html'

    def get_sessions(self):
        return Session.objects

class HomepageView(BuildableTemplateView):
    build_path = 'index.html'
    template_name = 'cocktail_summit/homepage.html'