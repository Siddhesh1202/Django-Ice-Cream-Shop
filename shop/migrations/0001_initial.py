# Generated by Django 3.0.5 on 2020-04-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('decription', models.CharField(max_length=300)),
                ('date', models.DateField()),
            ],
        ),
    ]
