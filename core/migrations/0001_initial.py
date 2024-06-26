# Generated by Django 5.0.6 on 2024-06-14 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('discipline_id', models.AutoField(primary_key=True, serialize=False)),
                ('discipline_name', models.CharField(max_length=30)),
                ('discipline_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalSpace',
            fields=[
                ('space_id', models.AutoField(primary_key=True, serialize=False)),
                ('space_floor', models.IntegerField()),
                ('space_number', models.IntegerField()),
                ('space_block', models.CharField(max_length=1)),
                ('space_type', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('siape', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('allocation_id', models.AutoField(primary_key=True, serialize=False)),
                ('days_week', models.CharField(max_length=10)),
                ('timetable', models.CharField(max_length=10)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.discipline')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.physicalspace')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher')),
            ],
        ),
    ]
