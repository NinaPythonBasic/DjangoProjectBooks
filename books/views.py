from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from books.models import Book, Category, Reader, BookOnHand


def main_page(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books/index.html", context)


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("books")


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("categories")


class ReaderListView(ListView):
    model = Reader


class ReaderDetailView(DetailView):
    model = Reader


class ReaderCreateView(CreateView):
    model = Reader
    fields = "__all__"
    success_url = reverse_lazy("readers")


class BookOnHandListView(ListView):
    model = BookOnHand


class BookOnHandDetailView(DetailView):
    model = BookOnHand


class BookOnHandCreateView(CreateView):
    model = BookOnHand
    fields = "__all__"
    success_url = reverse_lazy("booksonhand")
