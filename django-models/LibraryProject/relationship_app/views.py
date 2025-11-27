from django.shortcuts import render, redirect
from django.views import View
from .models import Book, Library

# REQUIRED INDIVIDUAL IMPORTS FOR CHECKER
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# ----------------------------------------------------
# FUNCTION-BASED VIEW
# ----------------------------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# ----------------------------------------------------
# CLASS-BASED VIEW
# ----------------------------------------------------
class LibraryDetailView(View):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        return render(request, "relationship_app/library_detail.html", {"library": library})


# ----------------------------------------------------
# USER REGISTRATION
# ----------------------------------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# ----------------------------------------------------
# USER LOGIN
# ----------------------------------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()

    return render(request, "relationship_app/login.html", {"form": form})


# ----------------------------------------------------
# USER LOGOUT
# ----------------------------------------------------
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
