from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

# We are creating a custom view for logout so that our user isn't redirected
# to the Django admin view, which can be confusing as it will have different
# UI
# This function logs out the user and redirects them to the home page
def logout_user(request):
    logout(request)
    return redirect(reverse('libraryapp:home'))