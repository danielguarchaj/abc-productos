# Generated by Django 3.2.18 on 2023-03-17 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='codigo',
        ),
    ]