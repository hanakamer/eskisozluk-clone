# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eksiapp', '0003_title_entry_of_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='author',
        ),
        migrations.AddField(
            model_name='title',
            name='author',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
