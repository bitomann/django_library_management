from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('library/', list_libraries, name='library'),
    path('library/form', library_form, name='library_form'),
    path('library/<int:library_id>/', library_details, name='library'),
    path('books/', book_list, name='books'),
    path('books/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('librarians/', list_librarians, name='librarians'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian')
]