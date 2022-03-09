from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Event, Resource
from .forms import MeetingForm, ResourceForm
from django.urls import reverse_lazy, reverse

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

class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testUser1', password='P@ssw0rd!')
        self.meeting=Meeting.objects.create(meetingtitle='Raises', meetingdate='2022-03-28', meetingtime='12:00:00', meetinglocation='Seattle', meetingagenda='testing agenda')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/pythonclubapp/newmeeting/')

