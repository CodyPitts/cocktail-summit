from __future__ import absolute_import

from django.core import management
from django.core.management.base import BaseCommand

from celery import Celery
from celery import shared_task

from django_medusa.renderers import StaticSiteRenderer
from django_medusa.utils import get_static_renderers
from django_medusa.settings import (MEDUSA_COLLECT_STATIC_IGNORE,
    MEDUSA_COLLECT_STATIC)


@shared_task
def publish():
    #call_command('staticsitegen', verbosity=0)

    StaticSiteRenderer.initialize_output()

    for Renderer in get_static_renderers():
        r = Renderer()
        r.generate()

    StaticSiteRenderer.finalize_output()