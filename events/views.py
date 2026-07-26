from django.shortcuts import render

def home(request):
    return render(request, 'events/home.html')


def event_list(request):
    return render(request, 'events/event_list.html')

