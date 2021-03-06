# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('roll', models.CharField(max_length=12)),
                ('department', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
