from django.core.management.base import BaseCommand
from books.models import Category, Book, Reader, BookOnHand

import datetime


class Command(BaseCommand):
    help = "Fill db"

    def handle(self, *args, **options):
        print("Удаляем старые данные")
        BookOnHand.objects.all().delete()
        Reader.objects.all().delete()
        Book.objects.all().delete()
        Category.objects.all().delete()

        print("Создаем новые данные")
        rus_category = Category.objects.create(name="Русская классика")
        foreign_category = Category.objects.create(name="Зарубежная классика")
        detective_category = Category.objects.create(name="Детектив")

        book1 = Book.objects.create(
            author="Тургенев Иван Сергеевич",
            name="Отцы и дети",
            category=rus_category,
            isbn="978-5-04-111268-4",
            publisher="Эксмо",
            year=2001,
            place='{"шкаф": 1, "полка": 3}',
            details="Помяты края",
        )

        book2 = Book.objects.create(
            author="Булгаков Михаил Афанасьевич",
            name="Мастер и Маргарита",
            category=rus_category,
            isbn="978-5-389-01686-6",
            publisher="АСТ",
            year=2006,
            place='{"шкаф": 2, "полка": 2}',
        )

        book3 = Book.objects.create(
            author="Лондон Джек",
            name="Мартин Иден",
            category=foreign_category,
            isbn="978-5-519-61774-1",
            publisher="Азбука",
            year=2007,
            place='{"шкаф": 3, "полка": 1}',
        )

        book4 = Book.objects.create(
            author="Лопе де Вега",
            name="Собака на сене",
            category=foreign_category,
            isbn="978-5-4467-1296-0",
            publisher="Треугольник",
            year=2016,
            place='{"шкаф": 3, "полка": 2}',
        )

        book5 = Book.objects.create(
            author="Дэн Браун",
            name="Инферно",
            category=detective_category,
            isbn="978-5-17-108451-6",
            publisher="АСТ",
            year=2020,
            place='{"шкаф": ,4 "полка": 10}',
        )

        reader1 = Reader.objects.create(
            name="Сидоров Василий Петрович",
            address="Санкт-Петербург, ул.Войкова, д.1, кв.5",
            phone="+79351112233",
        )

        reader2 = Reader.objects.create(
            name="Иванов Савелий Иванович",
            address="Санкт-Петербург, ул.Ботаническая, д.2, кв.13",
            phone="+79351112234",
        )

        reader3 = Reader.objects.create(
            name="Зеленкова Лариса Петровна",
            address="Санкт-Петербург, ул.Красноармейская, д.16/3, кв.65",
            phone="+79351112235",
        )

        reader4 = Reader.objects.create(
            name="Губаревич Анастасия Александровна",
            address="Санкт-Петербург, Ораниенбаумский пр., д.19 А, кв.309",
            phone="+79351112236",
        )

        bookonhand1 = BookOnHand.objects.create(
            book=book3, reader=reader2, issuedate=datetime.date(2022, 12, 30)
        )

        bookonhand2 = BookOnHand.objects.create(
            book=book5,
            reader=reader3,
            issuedate=datetime.date(2023, 2, 14),
            returndate=datetime.date(2023, 2, 25),
        )

        book3.onhand = True
        book3.save()
