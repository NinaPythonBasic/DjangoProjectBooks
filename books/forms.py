from django import forms
from .models import Book, Category, Reader


class BookModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookModelForm, self).__init__(*args, **kwargs)
        self.fields["author"].widget.attrs["size"] = 40
        self.fields["name"].widget.attrs["size"] = 40
        self.fields["publisher"].widget.attrs["size"] = 40
        self.fields["year"].widget.attrs["size"] = 40
        self.fields["place"].widget.attrs["size"] = 40
        self.fields["details"].widget.attrs["size"] = 40

    class Meta:
        model = Book
        fields = "__all__"


class ReaderModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReaderModelForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["size"] = 40
        self.fields["address"].widget.attrs["size"] = 40
        self.fields["phone"].widget.attrs["size"] = 40

    class Meta:
        model = Reader
        fields = "__all__"


class CategoryModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryModelForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["size"] = 40

    class Meta:
        model = Category
        fields = "__all__"
