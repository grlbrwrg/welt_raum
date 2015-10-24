# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anmeldungen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KW',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('kw', models.IntegerField()),
                ('jahr', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='events',
            name='jahr',
        ),
        migrations.AlterField(
            model_name='events',
            name='kw',
            field=models.ForeignKey(to='anmeldungen.KW'),
        ),
    ]
