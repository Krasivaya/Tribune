# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-05-14 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Editor')),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.tags'),
        ),
    ]
