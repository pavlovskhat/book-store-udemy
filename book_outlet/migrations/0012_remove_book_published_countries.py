# Generated by Django 4.2.6 on 2023-10-25 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0011_book_published_countries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_countries',
        ),
    ]
