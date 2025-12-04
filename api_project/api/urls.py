
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),   # old ListAPIView
    path('', include(router.urls)),                         # auto-generated CRUD routes
]
