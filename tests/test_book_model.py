"""Unit tests for book models/database."""
import pytest

from store.book.models import Book


@pytest.mark.usefixtures('db')
class TestBook:
    """Book test."""

    def test_get_by_isbn13(self):
        """Test can retrieve by isbn."""
        book = Book("book0", "Lalala", "Alvin Tan", "Penguin Books",
                    2016, 50, 25, "Text-only", "la", "Fiction")
        book.save()

        # this method is inherited from a class in database.py
        retrieved = Book.get_by_id(book.isbn13)
        assert retrieved == book

    def test_retrieve_list_of_books(self):
        """Test able to retrieve a list of books."""
        book0 = Book("book0", "Lalala", "Alvin Tan", "Penguin Books",
                     2016, 50, 25, "Text-only", "la", "Fiction")

        book1 = Book("book1", "Lololo", "Kelvin Tan", "Aweseom Books",
                     2009, 500, 50, "Text-Picture", "lo", "Non-Fiction")

        book_list = [book0, book1]

        # book_list.extend(BookFactory.create_batch(5))

        for book in book_list:
            book.save()
        i = Book.query.all()
        assert len(i) == 2

    def test_filter_books_by_subject(self):
        """Test filtering books by subject."""
        from store.dummy_data import books

        for b in books.sample_list:
            b.save()

        all_books = Book.query.all()
        assert len(all_books) > 0

        result = Book.query.filter_by(subject="romance").all()
        assert len(result) == 3
