from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import management
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic

from django_medusa.renderers import StaticSiteRenderer
from django_medusa.utils import get_static_renderers
from django_medusa.settings import (MEDUSA_COLLECT_STATIC_IGNORE,
    MEDUSA_COLLECT_STATIC)

from tasks import publish

from .models import Speaker, Sponsor, Session, Event

class PublishView(generic.base.View):
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        response_message = 'New site build successfully triggered'

        try:
            publish()

        except:
            response_message = 'Uh oh, there was a problem publishing the static pages'
        
        messages.add_message(request, messages.INFO, response_message)
        return HttpResponseRedirect(reverse('admin:index'))

class SpeakersView(generic.ListView):
    template_name = 'cocktail_summit/speakers.html'
    context_object_name = 'speaker_list'

    def dispatch(self, *args, **kwargs):
        self.slug = kwargs.get('slug', None)
        self.event = get_object_or_404(Event, slug=self.slug)
        self.sessions = Session.objects.filter(event=self.event)

        return super(SpeakersView, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        queryset = Speaker.objects.filter(session__in=self.sessions)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(SpeakersView, self).get_context_data(**kwargs)
        context['event'] = self.event

        return context


class SponsorsView(generic.ListView):
    template_name = 'cocktail_summit/sponsors.html'
    context_object_name = 'sponsor_list'

    def dispatch(self, *args, **kwargs):
        self.slug = kwargs.get('slug', None)
        self.event = get_object_or_404(Event, slug=self.slug)
        self.sponsors = Sponsor.objects.filter(event=self.event)

        return super(SponsorsView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = self.sponsors

        return queryset

    def get_context_data(self, **kwargs):
        context = super(SponsorsView, self).get_context_data(**kwargs)
        context['event'] = self.event

        return context

    """def get_sponsors(self):
        return Sponsor.objects"""

class SessionsView(generic.ListView):
    model = Session
    template_name = 'cocktail_summit/schedule.html'
    context_object_name = 'session_list'

    def get_sessions(self):
        return Session.objects

class HomepageView(generic.ListView):
    model = Event
    template_name = 'cocktail_summit/homepage.html'
    context_object_name = 'event_list'

    def get_events(self):
        return Event.objects

class TicketsView(generic.base.TemplateView):
    template_name = 'cocktail_summit/tickets.html'

class ContactView(generic.base.TemplateView):
    template_name = 'cocktail_summit/contact.html'

class ConductView(generic.base.TemplateView):
    template_name = 'cocktail_summit/conduct.html'

class EventBaseView(generic.DetailView):
    model = Event
    template_name = 'cocktail_summit/eventbase.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super(EventBaseView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, slug=slug)

        return context







