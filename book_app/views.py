
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import Books

def book(request):
  template = loader.get_template('books.html')
  myBooks = list(Books.objects.all().values()) #all data from books

  return JsonResponse(myBooks,safe=False)