# Generated by Django 4.2.11 on 2025-02-21 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
    ]
