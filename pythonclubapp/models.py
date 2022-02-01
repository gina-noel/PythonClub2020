from collections import UserList
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField(auto_now=False, auto_now_add=False)
    meetinglocation=models.TextField()
    meetingagenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingminutesid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingminutesattendance=models.ManyToManyField(User)
    meetingminutestext=models.TextField()

    def __str__(self):
        return self.meetingid

    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField()
    resourceURL=models.URLField(null=True, blank=True)
    resourcedateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField
    eventdate=models.DateField()
    eventtime=models.TimeField(auto_now=False, auto_now_add=False)
    eventdescription=models.TextField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return self.eventtitle

    class Meta:
        db_table='event'