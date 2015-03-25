# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20150321_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon_class_page',
            field=models.CharField(max_length=200, verbose_name=b'CSS icon (\xd0\xbd\xd0\xb0 \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb5)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='icon_page',
            field=models.ImageField(upload_to=b'static/uploads/', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0 (\xd0\xbd\xd0\xb0 \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb5)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to=b'static/uploads/', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0 (\xd0\xb2 \xd0\xbc\xd0\xb5\xd0\xbd\xd1\x8e)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='icon_class',
            field=models.CharField(max_length=200, verbose_name=b'CSS icon (\xd0\xb2 \xd0\xbc\xd0\xb5\xd0\xbd\xd1\x8e)', blank=True),
            preserve_default=True,
        ),
    ]
