import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Book
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def book_list(request):
    if request.method == 'GET':
        # opens, and then closes connection, because we use 'with'
        with sqlite3.connect(Connection.db_path) as conn:
            # make a row factory. sqlite3.Row bascially puts keys on our tuples
            conn.row_factory = sqlite3.Row
            # create a cursor object
            db_cursor = conn.cursor()

            # define the SQL Query, which will be saved on the cursor
            db_cursor.execute('''
            select
                b.id,
                b.title,
                b.isbn_number,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            ''')

            all_books = []
            # get the data
            dataset = db_cursor.fetchall()

            # loop through dataset, create book instances, append to all_books
            for row in dataset:
                book = Book()
                book.id= row['id']
                book.title = row['title']
                book.ISBN_number = row['isbn_number']
                book.author = row['author']
                book.year_published = row['year_published']
                book.librarian_id = row['librarian_id']
                book.location_id = row['location_id']

                all_books.append(book)

        # variable name template assigned to the path to our HTML template
        # that will be used for this view
        template = 'books/list.html'

        # dictionary of values passing into the template
        context = {
            'all_books': all_books
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, author, isbn_number,
                year_published, location_id, librarian_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['author'], form_data['isbn_number'],
            form_data['year_published'], request.user.id, form_data['location']))

        return redirect(reverse('libraryapp:books'))