# Generated by Django 3.0.5 on 2020-04-25 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
