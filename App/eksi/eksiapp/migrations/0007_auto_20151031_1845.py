# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eksiapp', '0006_entry_pub_date_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
