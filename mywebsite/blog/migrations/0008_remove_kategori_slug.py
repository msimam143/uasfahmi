# Generated by Django 4.1.4 on 2022-12-21 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_kategori_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategori',
            name='slug',
        ),
    ]