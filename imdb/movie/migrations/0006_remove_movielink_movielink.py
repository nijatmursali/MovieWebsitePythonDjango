# Generated by Django 3.0.4 on 2020-03-29 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200329_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielink',
            name='movielink',
        ),
    ]
