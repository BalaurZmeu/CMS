from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage


def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = FlatPage.objects.filter(content__icontains=query)
    
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search/search.html', context)
