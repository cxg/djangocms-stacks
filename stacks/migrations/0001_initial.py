# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', help_text='Descriptive name to identify this stack. Not displayed to users.', max_length=255, verbose_name='stack name', blank=True)),
                ('code', models.CharField(help_text='To render the stack in templates.', unique=True, max_length=255, verbose_name='stack code', blank=True)),
                ('content', cms.models.fields.PlaceholderField(related_name='stacks_contents', slotname='stack_content', editable=False, to='cms.Placeholder', null=True, verbose_name='stack content')),
            ],
            options={
                'verbose_name': 'stack',
                'verbose_name_plural': 'stacks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StackLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('stack', models.ForeignKey(verbose_name='stack', to='stacks.Stack')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
