# Generated by Django 3.2.16 on 2023-03-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0006_alter_book_isbn"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.CharField(max_length=20, verbose_name="ISBN"),
        ),
    ]
