# Generated by Django 2.1.2 on 2018-12-06 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Film ID')),
                ('imdb_id', models.CharField(blank=True, max_length=25, null=True, verbose_name='IMDB ID')),
                ('movie_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Film Adı')),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, verbose_name='Film Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Kayıt Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmler',
                'ordering': ('-created_at',),
            },
        ),
    ]
