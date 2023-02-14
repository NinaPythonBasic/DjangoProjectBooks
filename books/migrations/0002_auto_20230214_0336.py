# Generated by Django 3.2.16 on 2023-02-14 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(db_index=True, max_length=128, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.category', verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='details',
            field=models.TextField(default='', verbose_name='примечание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(db_index=True, max_length=256, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='book',
            name='onhand',
            field=models.BooleanField(default=False, verbose_name='книга выдана'),
        ),
        migrations.AlterField(
            model_name='book',
            name='place',
            field=models.CharField(max_length=256, verbose_name='место хранения'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=104, verbose_name='издательство'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(verbose_name='год издания'),
        ),
        migrations.AlterField(
            model_name='bookonhand',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', verbose_name='книга'),
        ),
        migrations.AlterField(
            model_name='bookonhand',
            name='details',
            field=models.TextField(default='', verbose_name='примечание'),
        ),
        migrations.AlterField(
            model_name='bookonhand',
            name='issuedate',
            field=models.DateField(verbose_name='дата выдачи'),
        ),
        migrations.AlterField(
            model_name='bookonhand',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.reader', verbose_name='читатель'),
        ),
        migrations.AlterField(
            model_name='bookonhand',
            name='returndate',
            field=models.DateField(null=True, verbose_name='дата возврата'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='address',
            field=models.CharField(max_length=256, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='name',
            field=models.CharField(db_index=True, max_length=184, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='телефон'),
        ),
    ]
