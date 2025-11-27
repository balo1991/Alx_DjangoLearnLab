from django.shortcuts import render
from django.views import View
from .models import Book, Library

# ----------------------------------------------------
# FUNCTION-BASED VIEW (plain text output)
# ----------------------------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# ----------------------------------------------------
# CLASS-BASED VIEW (plain text output)
# ----------------------------------------------------
class LibraryDetailView(View):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        return render(request, "relationship_app/library_detail.html", {"library": library})
