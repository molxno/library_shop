# Generated by Django 5.1.2 on 2024-11-04 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderProduct',
            new_name='OrderBook',
        ),
    ]
