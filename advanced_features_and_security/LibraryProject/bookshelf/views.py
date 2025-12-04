# bookshelf/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Display list of books with safe searching using ORM filtering.
    Prevents SQL injection by avoiding raw queries.
    """
    query = request.GET.get("q", "").strip()
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, "bookshelf/book_list.html", {"books": books})


@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    Create a new book using a secure Django form.
    Automatically validates and sanitizes input.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "bookshelf/form_example.html", {"form": form})


@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    Edit an existing book with safe form handling.
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "bookshelf/form_example.html", {"form": form})


@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    Secure deletion of books, protected by permissions.
    """
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")
