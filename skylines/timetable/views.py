from django.shortcuts import render
from django.http import HttpResponse

def shedule(request):
    return HttpResponse('do')

def main(request):
    return render(request, 'timetable/temp.html')
# Create your views here.
