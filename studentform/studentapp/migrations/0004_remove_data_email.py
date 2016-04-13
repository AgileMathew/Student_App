# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20160412_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='email',
        ),
    ]
