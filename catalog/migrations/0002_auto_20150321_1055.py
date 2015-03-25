# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to=b'static/uploads/', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='icon_class',
            field=models.CharField(max_length=200, verbose_name=b'CSS icon', blank=True),
            preserve_default=True,
        ),
    ]
