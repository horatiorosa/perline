# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151024185721 on 2015-11-05 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.URLField(max_length=50, unique=True)),
                ('link_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(verbose_name='Date Modified')),
                ('tags', models.TextField(verbose_name='tags')),
            ],
        ),
    ]