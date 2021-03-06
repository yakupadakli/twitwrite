# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True, verbose_name='Title')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Tweet')),
                ('signature', models.CharField(blank=True, max_length=32, null=True, verbose_name='Signature')),
            ],
        ),
    ]
