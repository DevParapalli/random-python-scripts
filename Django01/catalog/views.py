from django.shortcuts import render

# imports the models 
from catalog.models import Book, BookInstance, Author, Genre
# Create your views here.
def index(request):
    """View function for simple home page"""
    
    # generate count of main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_available_instances = BookInstance.objects.filter(status__exact='a').count()
    
    # the all() is implied by default but still using it.
    num_authors = Author.objects.all().count()
    
    context = {
        'num_books' : num_books,
        'num_instances': num_instances,
        'num_available_instances' : num_available_instances,
        'num_authors' : num_authors,
    }
    
    # render the HTML Template 
    return render(request, 'catalog/index.html', context=context)
