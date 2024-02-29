# Generated by Django 5.0.1 on 2024-02-29 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='league_table',
            fields=[
                ('league_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('league_img_url', models.CharField(max_length=1000)),
                ('source_system_id', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='stat_type_table',
            fields=[
                ('stat_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=100)),
                ('lookup_name', models.CharField(max_length=100)),
                ('group_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='division_table',
            fields=[
                ('division_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('source_system_id', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strozone.league_table')),
            ],
        ),
        migrations.CreateModel(
            name='team_table',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city_name', models.CharField(max_length=100)),
                ('team_img_url', models.CharField(max_length=1000)),
                ('source_system_id', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strozone.division_table')),
            ],
        ),
    ]
