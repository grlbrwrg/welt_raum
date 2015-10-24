# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('jahr', models.IntegerField()),
                ('kw', models.IntegerField()),
                ('titel', models.CharField(max_length=200)),
                ('beschreibung', models.CharField(max_length=600)),
                ('termin', models.DateTimeField()),
                ('strasse', models.CharField(max_length=140)),
                ('plz', models.IntegerField()),
                ('ort', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nutzer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=600)),
                ('datum', models.DateField(auto_now_add=True)),
                ('events', models.ManyToManyField(to='anmeldungen.Events')),
            ],
        ),
    ]
