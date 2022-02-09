from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event, User

# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')

# all may not be a good idea if you have a lot! 
def resources(request):
    resource_list=Resource.objects.all() 
    return render(request, 'pythonclubapp/resources.html', {'resource_list' : resource_list})

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'pythonclubapp/meetings.html', {'meeting_list':meeting_list})
    
def meetingdetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'pythonclubapp/meetingdetail.html', {'meeting' : meeting})