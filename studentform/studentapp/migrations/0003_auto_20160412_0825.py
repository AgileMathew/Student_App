# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_auto_20160412_0721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='gmail',
            new_name='email',
        ),
    ]
