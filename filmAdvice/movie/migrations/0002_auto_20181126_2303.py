# Generated by Django 2.1.2 on 2018-11-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='IMDB ID'),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='Film ID'),
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_name',
            field=models.CharField(default='', max_length=150, verbose_name='Film Adı'),
        ),
    ]
