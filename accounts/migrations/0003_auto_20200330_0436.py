# Generated by Django 3.0.4 on 2020-03-29 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_default_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('', ''), ('Female', 'Female'), ('male', 'Male')], max_length=50),
        ),
    ]
