# Generated by Django 3.0.5 on 2020-04-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msgid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('decs', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='decription',
            new_name='description',
        ),
    ]
