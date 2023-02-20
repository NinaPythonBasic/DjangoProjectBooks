from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from books.models import Book, Category, Reader, BookOnHand
from .forms import BookModelForm, ReaderModelForm, CategoryModelForm


def main_page(request):
    return render(request, "books/index.html")


class BookListView(ListView):
    model = Book

    def get_queryset(self):
        filter_str = self.request.GET.get("q")
        if filter_str is None:
            result_list = Book.objects.all()
        else:
            result_list = Book.objects.filter(
                Q(name__icontains=filter_str) | Q(author__icontains=filter_str)
            )
        return result_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        filter_str = self.request.GET.get("q")
        context["q"] = filter_str
        return context


class BookDetailView(DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookModelForm
    success_url = reverse_lazy("books")


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookModelForm
    success_url = reverse_lazy("books")


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("books")


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryModelForm
    success_url = reverse_lazy("categories")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryModelForm
    success_url = reverse_lazy("categories")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("categories")


class ReaderListView(LoginRequiredMixin, ListView):
    model = Reader

    def get_queryset(self):
        filter_str = self.request.GET.get("q")
        if filter_str is None:
            result_list = Reader.objects.all()
        else:
            result_list = Reader.objects.filter(name__icontains=filter_str)
        return result_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        filter_str = self.request.GET.get("q")
        context["q"] = filter_str
        return context


class ReaderDetailView(LoginRequiredMixin, DetailView):
    model = Reader


class ReaderCreateView(LoginRequiredMixin, CreateView):
    model = Reader
    # fields = "__all__"
    form_class = ReaderModelForm
    success_url = reverse_lazy("readers")


class ReaderUpdateView(LoginRequiredMixin, UpdateView):
    model = Reader
    # fields = "__all__"
    form_class = ReaderModelForm
    success_url = reverse_lazy("readers")


class ReaderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reader
    success_url = reverse_lazy("readers")


class BookOnHandListView(LoginRequiredMixin, ListView):
    model = BookOnHand

    def get_queryset(self):
        filter_str = self.request.GET.get("q")
        if filter_str is None:
            result_list = BookOnHand.objects.all()
        else:
            result_list = BookOnHand.objects.filter(
                Q(book__name__icontains=filter_str)
                | Q(reader__name__icontains=filter_str)
            )
        return result_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        filter_str = self.request.GET.get("q")
        context["q"] = filter_str
        return context


#
class BookOnHandDetailView(LoginRequiredMixin, DetailView):
    model = BookOnHand


class BookOnHandCreateView(LoginRequiredMixin, CreateView):
    model = BookOnHand
    fields = "__all__"
    success_url = reverse_lazy("booksonhand")


class BookOnHandUpdateView(LoginRequiredMixin, UpdateView):
    model = BookOnHand
    fields = "__all__"
    success_url = reverse_lazy("booksonhand")


class BookOnHandDeleteView(LoginRequiredMixin, DeleteView):
    model = BookOnHand
    success_url = reverse_lazy("booksonhand")
