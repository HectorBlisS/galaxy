# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 19:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth', models.DateField(blank=True, null=True)),
                ('tel', models.IntegerField(blank=True, default=0, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('avatar', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]