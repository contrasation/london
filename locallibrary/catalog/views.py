from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
# Create your views here.

def index(request):

    """
    View function for home page of site.
    :param request:
    :return:
    """
    # Generate counts of some of the main objects.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status_exact='a').count()
    num_authors = Author.objects.count() # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        countext = {'num_books': num_books, 'num_instances': num_instances,
                    'num_instances_availabel': num_instances_available,
                    'num_authors': num_authors},
    )