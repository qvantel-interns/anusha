# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsstest', '0003_auto_20160620_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bsstest',
            name='city',
        ),
    ]
