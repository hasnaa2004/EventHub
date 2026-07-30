from django.shortcuts import render
from .models import Event

def events_list_view(request):
    
    raw_search = request.GET.get('q', '')
    selected_category = request.GET.get('category', '')
    sort_criteria = request.GET.get('sort', 'title')

   
    cleaned_query = raw_search.strip()              
    lower_query = cleaned_query.lower()           
    replaced_query = lower_query.replace('  ', ' ')
    upper_query = replaced_query.upper()            
    title_query = replaced_query.title()            
   
    events = Event.objects.all()

    
    if lower_query:
        events = events.filter(title__icontains=lower_query)

    if selected_category:
        events = events.filter(category=selected_category)

   
    events = events.exclude(status='cancelled')

   
    if sort_criteria == 'az':
        events = events.order_by('title')
    elif sort_criteria == 'za':
        events = events.order_by('-title')
    else:
        events = events.order_by('-date')

    events = events.distinct()

   
    has_results = events.exists()

   
    total_results_count = events.count()

    context = {
        'events': events,
        'has_results': has_results,
        'total_count': total_results_count,
        'query': lower_query,
    }

    return render(request, 'events/events_list.html', context)