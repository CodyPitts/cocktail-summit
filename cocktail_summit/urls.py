"""cocktail_summit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(
        '^', include('django.contrib.auth.urls')
    ),

    url(r'^admin_tools/', include('admin_tools.urls')),

    url(
        regex = '^$',
        view = views.HomepageView.as_view(),
        kwargs = {},
        name = 'eventlist',
    ),

    url(
        regex = '^(?P<slug>[-\w]+)/$',
        view = views.EventBaseView.as_view(),
        kwargs = {},
        name = 'eventbase',
    ),

    url(
        regex = '^(?P<slug>[-\w]+)/speakers/$',
        view = views.SpeakersView.as_view(),
        kwargs = {},
        name = 'speakers',
    ),

    url(
        regex = '^(?P<slug>[-\w]+)/sponsors/$',
        view = views.SponsorsView.as_view(),
        kwargs = {},
        name = 'sponsors',
    ),

    url(
        regex = '^(?P<slug>[-\w]+)/schedule/$',
        view = views.SessionsView.as_view(),
        kwargs = {},
        name = 'schedule',
    ),

    url(
        regex = '^(?P<slug>[-\w]+)/tickets/$',
        view = views.TicketsView.as_view(),
        kwargs = {},
        name = 'tickets',
    ),

    url(
        regex = '^publish/$',
        view = views.PublishView.as_view(),
        kwargs = {},
        name = 'publish',
    ),

    url(
        regex = '^contact/$',
        view = views.ContactView.as_view(),
        kwargs = {},
        name = 'contact',
    ),

    url(
        regex = '^conduct/$',
        view = views.ConductView.as_view(),
        kwargs = {},
        name = 'conduct',
    ),
    
]








