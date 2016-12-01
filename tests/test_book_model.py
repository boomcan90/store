"""Unit tests for book models/database"""
import datetime as t
import pytest

from store.book.models import Book
from .factories import BookFactory
from store.dummy_data import books as testdata

@pytest.mark.usefixtures('db')
class TestBookModel:
    """Book test"""

    def test_get_by_isbn13(self):
        book = Book("book0", "Lalala", "Alvin Tan","Penguin Books",
            2016 ,50 ,25 ,"Text-only","la","Fiction")
        book.save()

        # this method is inherited from a class in database.py
        retrieved = Book.get_by_id(book.isbn13)
        assert retrieved == book

    def test_retrieve_list_of_books(self):

        book0 = Book("book0", "Lalala", "Alvin Tan","Penguin Books",
            2016 ,50 ,25 ,"Text-only","la","Fiction")

        book1 = Book("book1", "Lololo", "Kelvin Tan","Aweseom Books",
            2009 ,500 ,50 ,"Text-Picture","lo","Non-Fiction")


        book_list = [book0,book1]

        # book_list.extend(BookFactory.create_batch(5))

        for book in book_list:
            book.save()
        i = Book.query.all()
        assert len(i) == 2


    def test_query_returns_correct_book(self):
        book0 = Book("book0", "Lalala", "Alvin Tan","Penguin Books",
            2016 ,50 ,25 ,"Text-only","la","romance")

        book1 = Book("book1", "Lololo", "Kelvin Tan","Aweseome Books",
            2009 ,500 ,50 ,"Text-Picture","lo","romance")


        book_list = [book0,book1]


        for book in book_list:
            book.save()
        
        # i = Book.query.filter_by(subject='Non-Fiction').all()
        # assert len(i) == 1

        # for book in testdata.sample_list:
        #     book.save()

        i = Book.query.filter_by(subject='romance').all()
        assert len(i) == 2
        # books = Book.query.filter_by(Book.isbn13.contains('9780439358071')).all()

