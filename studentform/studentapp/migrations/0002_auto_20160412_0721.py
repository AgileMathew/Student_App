# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='data',
            name='rollno',
            field=models.CharField(max_length=400),
            preserve_default=True,
        ),
    ]
