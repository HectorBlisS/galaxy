# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 21:22
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_subject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
