# Generated by Django 3.0.4 on 2020-03-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(default='Kv6b5JeAlw6R8Q1gD3wM4NOF6jgFN64a', max_length=32),
        ),
    ]
