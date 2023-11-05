from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def add_book(request):
    list_books = [
        ['A. Pushkin', 'Ruslan and Ludmila', '2016-12-06'],
        ['A. Pushkin', 'Revizor', '2016-12-06'],
        ['A. Duma', 'Paris', '2018-02-27'],
        ['Tutchev', 'Proza', '2018-02-27'],
        ['M. Gorkiy', 'Stories', '2019-02-22'],
        ['M. Gorkiy', 'Revolution', '2019-02-22'],
        ['M. Bulgakov', 'Master and Margo', '2019-02-22']
    ]
    for one_book in list_books :
        Book.objects.create(author= one_book[0], name= one_book[1], pub_date= one_book[2])

def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def books(request):
    book_object = Book.objects.all()
    list_books = [f'{book.name}, {book.author}, {book.pub_date}' for book in book_object]
    context = {
        'l_books' : list_books,
    }
    # return render(request, 'books/books.html', context)
    
    
    return HttpResponse(list_books)
    
def search_date(request, date):
    book_object = Book.objects.filter(pub_date = date)
    books = [f'{book.name}, {book.author}, {book.pub_date}' for book in book_object]
    return HttpResponse(books)


# 2021-05-05