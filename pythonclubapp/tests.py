from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Event, Resource
from .forms import MeetingForm, ResourceForm

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Initial Club Meeting')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Initial Club Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type=MeetingMinutes(meetingminutestext='meeting 123')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'meeting 123')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(resourcename='Django Web Framework')

    def test_typestring(self):
        self.assertEqual(str(self.name), 'Django Web Framework')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle='Halloween Party')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Halloween Party')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class NewResourceForm(TestCase):
    # valid form data
    def test_resourceform(self):
        form=ResourceForm (data={'resourcename':'testName', 'resourcetype':'testType', 'resourceurl':'testURL', 'resourcedateentered':'2022-02-28', 'userid':'testUser', 'resourcedescription':'testDescription'})
        self.assertTrue(form.is_valid)

class NewMeetingForm(TestCase):
    # valid form data
    def test_meetingform(self):
        data={
            'meetingtitle':'testTitle', 
            'meetingdate':'2022-02-28', 
            'meetingtime':'12:00:00', 
            'meetinglocation':'testLocation', 
            'meetingagenda':'testAgenda'
            }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

