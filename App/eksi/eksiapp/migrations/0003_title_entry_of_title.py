# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eksiapp', '0002_auto_20151028_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='entry_of_title',
            field=models.ManyToManyField(related_name='Title', to='eksiapp.Entry'),
        ),
    ]
