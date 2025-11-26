# CRUD Operations for Book Model

---

## CREATE
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell>

---

## RETRIEVE
book = Book.objects.get(title="1984")
book.title    # "1984"
book.author   # "George Orwell"
book.publication_year  # 1949

---

## UPDATE
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title   # "Nineteen Eighty-Four"

---

## DELETE
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()   # <QuerySet []>
