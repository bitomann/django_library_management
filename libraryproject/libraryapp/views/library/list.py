import sqlite3
from django.shortcuts import render
from libraryapp.models import Library
from ..connection import Connection


def library(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.title,
            l.address,
        from libraryapp_library l
        join auth_user u on l.user_id = u.id
        """)

        the_library = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            lib = Library()
            lib.id = row["id"]
            lib.title_id = row["title_id"]
            lib.address_id = row["address_id"]

            library.append(lib)

    template_name = 'library/list.html'

    context = {
        'library': library
    }

    return render(request, template_name, context)