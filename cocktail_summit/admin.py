from django.contrib import admin
from .models import Speaker, Sponsor, Session, Event

admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Session)
admin.site.register(Event)