# Generated by Django 3.0.5 on 2020-04-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200423_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('address_1', models.CharField(max_length=500)),
                ('address_2', models.CharField(max_length=500)),
                ('phone', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('zip_code', models.CharField(max_length=500)),
            ],
        ),
    ]
