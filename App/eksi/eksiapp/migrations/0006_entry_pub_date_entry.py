# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eksiapp', '0005_auto_20151028_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='pub_date_entry',
            field=models.DateTimeField(verbose_name='date published', null=True),
        ),
    ]
