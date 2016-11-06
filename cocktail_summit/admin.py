from django.contrib import admin
from .models import Speaker, Sponsor, Session, Event, OffsiteSession

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("city",)}

admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Session)
admin.site.register(Event, EventAdmin)
admin.site.register(OffsiteSession)