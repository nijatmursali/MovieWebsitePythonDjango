# Generated by Django 3.0.4 on 2020-03-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200326_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='countryofprod',
            field=models.CharField(default='', max_length=100),
        ),
    ]
