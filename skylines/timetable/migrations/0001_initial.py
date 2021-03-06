# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('free_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.CharField(max_length=10)),
                ('arrival_time', models.CharField(max_length=10)),
                ('departure_date', models.CharField(max_length=15)),
                ('arrival_date', models.CharField(max_length=15)),
                ('place_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport', to='timetable.Airport')),
                ('place_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport', to='timetable.Airport')),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Airplane')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('access_level', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Timetable'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.User'),
        ),
    ]
