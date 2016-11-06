import datetime
from datetime import timedelta
from django.utils import timezone
from django.db import models

# after changing models, make new migrations
# will sometimes require either a DB reset or a nullable/blankable field, due to existing rows


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    city = models.CharField(max_length=50)
    slug = models.SlugField(help_text='The URL piece that identifies this event, e.g. `cocktailsummit.com/spokane`')
    description = models.TextField(blank=True)
    venue = models.CharField(max_length = 50, blank=True)
    state = models.CharField(max_length=20, blank=True)
    day_one_blurb = models.TextField(blank=True)
    day_two_blurb = models.TextField(blank=True)

    def __str__(self):
        return self.event_name

    def distinct_dates(self):
        #TODO: write a method that returns a list of the distinct
        #dates that this event has
        return []


class Speaker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    affiliation = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Sponsor(models.Model):
    logo = models.ImageField(blank=True)
    name = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    event = models.ManyToManyField(Event, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Session(models.Model):# Add session blocks
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    room = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    sponsor = models.ManyToManyField(Sponsor, blank=True)
    speakers = models.ManyToManyField(Speaker, blank=True)
    event = models.ForeignKey(Event)

    def __str__(self):
        return self.title

class OffsiteSession(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    room = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    sponsor = models.ManyToManyField(Sponsor, blank=True)
    speakers = models.ManyToManyField(Speaker, blank=True)
    event = models.ForeignKey(Event)
    location = models.TextField(blank=True)

    def __str__(self):
        return self.title









