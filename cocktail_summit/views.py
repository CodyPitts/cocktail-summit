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

from .models import Speaker, Sponsor, Session

class PublishView(generic.base.View):
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        response_message = 'Build triggered!'

        try:
            management.call_command('staticsitegen', verbosity=0)

            """StaticSiteRenderer.initialize_output()

            for Renderer in get_static_renderers():
                r = Renderer()
                r.generate()

            StaticSiteRenderer.finalize_output()

            if MEDUSA_COLLECT_STATIC:
                # collect static media for deployment
                call_command('collectstatic', interactive=False,
                    ignore_patterns=MEDUSA_COLLECT_STATIC_IGNORE)"""

        except:
            response_message = 'Uh oh there was a problem'
        
        if self.request.is_ajax():
            result = {'message': response_message}
            return self.render_json_to_response(result)
        else:
            return HttpResponse(response_message)

class SpeakersView(generic.ListView):
    model = Speaker
    template_name = 'cocktail_summit/speakers.html'
    context_object_name = 'speaker_list'

class SponsorsView(generic.ListView):
    model = Sponsor
    template_name = 'cocktail_summit/sponsors.html'
    context_object_name = 'sponsor_list'

    def get_sponsors(self):
        return Sponsor.objects

class SessionsView(generic.ListView):
    model = Session
    template_name = 'cocktail_summit/schedule.html'
    context_object_name = 'session_list'

    def get_sessions(self):
        return Session.objects

class HomepageView(generic.base.TemplateView):
    template_name = 'cocktail_summit/homepage.html'