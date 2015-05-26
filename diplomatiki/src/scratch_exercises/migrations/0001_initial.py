# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Epilogi',
                'verbose_name_plural': 'Epiloges',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default=b'C:\\pollsSite\\mysite\\media\\photos\\scratch logo.jpg', upload_to=b'photos')),
                ('difficulty', models.SmallIntegerField(default=2, verbose_name='Difficulty', choices=[(1, 'easy'), (2, 'normal'), (3, 'hard')])),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_updated', models.DateTimeField(editable=False)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='scratch_exercises.Category', verbose_name='\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': '\u0386\u03c3\u03ba\u03b7\u03c3\u03b7',
                'verbose_name_plural': '\u0386\u03c3\u03ba\u03ae\u03c3\u03b5\u03b9\u03c2',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='scratch_exercises.Question'),
            preserve_default=True,
        ),
    ]
