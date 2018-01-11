# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_remove_todo_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_to',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
