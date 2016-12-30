# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('sportType', models.CharField(max_length=30)),
                ('prizeCount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='teamID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
