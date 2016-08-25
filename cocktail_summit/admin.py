from django.contrib import admin
from .models import Speaker, Sponsor, Session

admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Session)