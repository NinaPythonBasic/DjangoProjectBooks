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
from .forms import (
    BookModelForm,
    ReaderModelForm,
    CategoryModelForm,
    BookOnHandUpdateModelForm,
    BookOnHandCreateModelForm,
)


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


def update_onhand(book_id, len_of_booksonhand):
    book = Book.objects.get(pk=book_id)
    if len_of_booksonhand > 0:
        book.onhand = True
    else:
        book.onhand = False
    book.save()


def set_onhand(updated_object):
    if (updated_object.issuedate is not None) and (updated_object.returndate is None):
        book_object = Book.objects.get(pk=updated_object.book.id)
        book_object.onhand = True
        book_object.save()
    else:
        data = BookOnHand.objects.filter(
            book__id=updated_object.book.id,
            issuedate__isnull=False,
            returndate__isnull=True,
        ).exclude(id=updated_object.id)
        update_onhand(updated_object.book.id, len(data))


class BookOnHandCreateView(LoginRequiredMixin, CreateView):
    model = BookOnHand
    form_class = BookOnHandCreateModelForm
    success_url = reverse_lazy("booksonhand")

    def form_valid(self, form):
        # Перед сохранением формы
        updated_object = form.save()
        set_onhand(updated_object)
        return super().form_valid(form)


class BookOnHandUpdateView(LoginRequiredMixin, UpdateView):
    model = BookOnHand
    form_class = BookOnHandUpdateModelForm
    success_url = reverse_lazy("booksonhand")

    def form_valid(self, form):
        # Перед сохранением формы
        updated_object = form.save()
        set_onhand(updated_object)
        return super().form_valid(form)


class BookOnHandDeleteView(LoginRequiredMixin, DeleteView):
    model = BookOnHand
    success_url = reverse_lazy("booksonhand")

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        data = BookOnHand.objects.filter(
            book__id=obj.book.id, issuedate__isnull=False, returndate__isnull=True
        ).exclude(id=obj.id)
        update_onhand(obj.book.id, len(data))

        return super().delete(request, *args, **kwargs)
