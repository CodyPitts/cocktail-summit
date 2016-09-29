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
    city = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.event_name


class Speaker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(blank=True)
    affiliation = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Sponsor(models.Model):
    logo = models.ImageField(blank=True)
    name = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    event = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    room = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    sponsor = models.ForeignKey(Sponsor, blank=True)
    speakers = models.ManyToManyField(Speaker, blank=True)
    event = models.ForeignKey(Event)

    def __str__(self):
        return self.title







