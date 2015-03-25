# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20150322_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('url', models.CharField(max_length=200, verbose_name=b'Url', blank=True)),
                ('text', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('view_count', models.IntegerField(default=0, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd1\x8b')),
                ('preview', models.ImageField(upload_to=b'static/uploads/', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8c\xd1\x8e', blank=True)),
                ('category', models.ForeignKey(default=b'-1', blank=True, to='catalog.Video', null=True, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
