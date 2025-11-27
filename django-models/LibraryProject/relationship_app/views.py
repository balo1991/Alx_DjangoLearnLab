from django.http import HttpResponse
from django.views import View
from .models import Book, Library


# ----------------------------------------------------
# FUNCTION-BASED VIEW (plain text output)
# ----------------------------------------------------
def list_books(request):
    books = Book.objects.all()

    output = ""
    for book in books:
        output += f"{book.title} by {book.author.name}\n"

    return HttpResponse(output, content_type="text/plain")


# ----------------------------------------------------
# CLASS-BASED VIEW (plain text output)
# ----------------------------------------------------
class LibraryDetailView(View):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        books = library.books.all()

        output = f"Library: {library.name}\nBooks:\n"
        for book in books:
            output += f"- {book.title} by {book.author.name}\n"

        return HttpResponse(output, content_type="text/plain")
