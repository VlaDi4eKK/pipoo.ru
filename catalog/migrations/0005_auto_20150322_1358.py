# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ForeignKey(default=b'-1', blank=True, to='catalog.Category', null=True, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
    ]
