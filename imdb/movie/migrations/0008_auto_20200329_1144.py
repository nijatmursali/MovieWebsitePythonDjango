# Generated by Django 3.0.4 on 2020-03-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_trailerlink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='trailerLink',
            new_name='trailerlink',
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.FloatField(default=0),
        ),
    ]
