# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsstest', '0002_auto_20160620_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bsstest',
            name='mobilenumber',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
