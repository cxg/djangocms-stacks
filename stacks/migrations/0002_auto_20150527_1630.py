# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('stacks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stacklink',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='stacklink',
            name='stack',
        ),
        migrations.DeleteModel(
            name='StackLink',
        ),
    ]
