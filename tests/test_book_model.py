"""Unit tests for book models/database."""
import pytest

from store.book.models import Book


@pytest.mark.usefixtures('db')
class TestBook:
    """Book test."""

    def test_get_by_isbn13(self):
        """Test can retrieve by isbn."""
        book = Book("book0", "Lalala", "Alvin Tan", "Penguin Books",
                    2016, 50, 25, "hardcover", "la", "Fiction")
        book.save()

        # this method is inherited from a class in database.py
        retrieved = Book.get_by_id(book.isbn13)
        assert retrieved == book

    def test_retrieve_list_of_books(self):
        """Test able to retrieve a list of books."""
        book0 = Book("book1", "Lalala", "Alvin Tan", "Penguin Books",
                     2016, 50, 25, "Text-only", "la", "Fiction")

        book1 = Book("book2", "Lololo", "Kelvin Tan", "Aweseom Books",
                     2009, 500, 50, "paperback", "lo", "Non-Fiction")

        book_list = [book0, book1]

        for book in book_list:
            book.save()
        i = Book.query.all()
        assert len(i) == 2

    def test_filter_books_by_subject(self):
        """Test filtering books by subject."""
        b1 = Book('9780439708180', "Harry Potter and the Philosopher's Stone",
                  "J. K. Rowling", "Scholastic", 1999, 10, 6.79, "paperback", "fantasy", "fantasy")

        b2 = Book('9780439064873', "Harry Potter And The Chamber Of Secrets",
                  "J. K. Rowling", "Scholastic", 2000, 8, 6.70, "paperback", "fantasy", "fantasy")

        b3 = Book('9780439136358', "Harry Potter And The Prisoner Of Azkaban",
                  "J. K. Rowling", "Scholastic", 1999, 11, 15.24, "hardcover", "fantasy", "fantasy")

        b4 = Book('9780439139595', "Harry Potter And The Goblet Of Fire",
                  "J. K. Rowling", "Scholastic", 2000, 9, 18.28, "hardcover", "fantasy", "fantasy")

        b5 = Book('9780439358071', "Harry Potter And The Order Of The Phoenix",
                  "J. K. Rowling", "Scholastic", 2004, 10, 7.86, "paperback", "fantasy", "fantasy")

        b6 = Book('9780439784542', "Harry Potter and the Half-Blood Prince",
                  "J. K. Rowling", "Scholastic", 2005, 5, 16.94, "hardcover", "fantasy", "fantasy")

        b7 = Book('9780545139700', "Harry Potter and the Deathly Hallows",
                  "J. K. Rowling", "Scholastic", 2007, 4, 9.14, "paperback", "fantasy", "fantasy")

        b8 = Book('9780345803481',
                  "Fifty Shades of Grey: Book One of the Fifty Shades Trilogy (Fifty Shades of Grey Series)",
                  "E L James", "Vintage Books", 2012, 7, 9.99, "paperback", "romance", "romance")

        b9 = Book('9780345803498', "Fifty Shades Darker",
                  "E L James", "Vintage Books", 2012, 7, 10.99, "paperback", "romance", "romance")

        b10 = Book('9780345803504',
                   "Fifty Shades Freed: Book Three of the Fifty Shades Trilogy (Fifty Shades of Grey Series)",
                   "E L James", "Vintage Books", 2012, 7, 9.59, "paperback", "romance", "romance")

        sample_list = []
        sample_list.append(b1)
        sample_list.append(b2)
        sample_list.append(b3)
        sample_list.append(b4)
        sample_list.append(b5)
        sample_list.append(b6)
        sample_list.append(b7)
        sample_list.append(b8)
        sample_list.append(b9)
        sample_list.append(b10)

        for b in sample_list:
            b.save()

        all_books = Book.query.all()
        assert len(all_books) > 0

        result = Book.query.filter_by(subject="romance").all()
        assert len(result) == 3
