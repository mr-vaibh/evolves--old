# Generated by Django 3.0.4 on 2020-03-29 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200330_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(default='VRJD3VssuE0dMhFIAN1W8aH6qx3T3RU6', max_length=32),
        ),
    ]