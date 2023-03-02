from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name="название", max_length=128, blank=False, null=False
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Book(models.Model):
    author = models.CharField(
        verbose_name="автор", max_length=128, blank=False, db_index=True
    )
    name = models.CharField(
        verbose_name="название", max_length=256, blank=False, db_index=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="жанр"
    )
    isbn = models.CharField(verbose_name="ISBN", max_length=20)
    publisher = models.CharField(verbose_name="издательство", max_length=104)
    year = models.IntegerField(verbose_name="год издания")
    place = models.CharField(verbose_name="место хранения", max_length=256)
    details = models.TextField(verbose_name="примечание", default="", blank=True)
    onhand = models.BooleanField(verbose_name="книга выдана", default=False)

    def __str__(self):
        return f"{self.id} {self.name} ({self.author})"

    def __repr__(self):
        return str(self)


class Reader(models.Model):
    name = models.CharField(
        verbose_name="ФИО",
        max_length=184,
        blank=False,
        db_index=True,
    )
    address = models.CharField(verbose_name="адрес", max_length=256)
    phone = models.CharField(verbose_name="телефон", max_length=12)

    def __str__(self):
        return f"{self.id} {self.name}"


class BookOnHand(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, verbose_name="книга")
    reader = models.ForeignKey(
        Reader, on_delete=models.PROTECT, verbose_name="читатель"
    )
    issuedate = models.DateField(verbose_name="дата выдачи")
    returndate = models.DateField(verbose_name="дата возврата", null=True, blank=True)
    details = models.TextField(verbose_name="примечание", default="", blank=True)

    def __str__(self):
        if self.returndate is None:
            returndate = ""
        else:
            returndate = self.returndate.strftime("%b. %d, %Y")
        issuedate = self.issuedate.strftime("%b. %d, %Y")
        return f"{self.reader.name}: {self.book.name} ({issuedate} - {returndate})"
