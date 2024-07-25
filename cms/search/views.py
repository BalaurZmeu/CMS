from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage


def search(request):
    """
    Search view. Retrieves the search query from the request and
    performs a case-insensitive search on the content of all
    FlatPage objects. Returns a rendered HTML template with
    the search query and the search results.
    """
    query = request.GET.get('q', '')
    results = []
    if query:
        results = FlatPage.objects.filter(content__icontains=query)
    context = {'query': query, 'results': results}
    return render(request, 'search/search.html', context)
