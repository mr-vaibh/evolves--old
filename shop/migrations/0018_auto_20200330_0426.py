# Generated by Django 3.0.4 on 2020-03-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200330_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(default='k1Hj1BpNxLtCqO1CTZMphbZY5m4txiG9', max_length=32),
        ),
    ]