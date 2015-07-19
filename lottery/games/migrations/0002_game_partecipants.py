# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('partecipation', '0001_initial'),
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='partecipants',
            field=models.ManyToManyField(related_name='game_partecipant', through='partecipation.Partecipation', to=settings.AUTH_USER_MODEL),
        ),
    ]
