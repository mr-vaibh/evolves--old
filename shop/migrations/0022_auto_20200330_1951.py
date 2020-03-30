# Generated by Django 3.0.4 on 2020-03-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20200330_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.PositiveSmallIntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(default='YEL6zCaTjtc4HKOjPaDZhiGc1CJxR4qg', max_length=32),
        ),
    ]