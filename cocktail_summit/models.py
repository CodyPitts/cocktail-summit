import datetime
from datetime import timedelta
from django.utils import timezone
from django.db import models


class Speaker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    photo = models.ImageField()

    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


class Sponsor(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name


class Session(models.Model):
    title = models.CharField(max_length=200)
    scheduled_time = models.DateTimeField()
    room = models.CharField(max_length=200)
    summary = models.TextField()
    sponsor = models.ForeignKey(Sponsor)
    speakers = models.ManyToManyField(Speaker)

    def __str__(self):
        return self.title







