# Generated by Django 3.0.4 on 2020-03-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20200330_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.PositiveIntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(default='yVbCQE6yF8pXubk5z1ap9rRaZ1pTgqaZ', max_length=32),
        ),
    ]
