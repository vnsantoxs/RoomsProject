# Generated by Django 5.0.6 on 2024-06-29 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaysWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('SEG', 'Segunda-feira'), ('TER', 'Terça-feira'), ('QUA', 'Quarta-feira'), ('QUI', 'Quinta-feira'), ('SEX', 'Sexta-feira'), ('SAB', 'Sábado'), ('DOM', 'Domingo')], max_length=3, unique=True)),
                ('descricao', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='allocation',
            name='days_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.daysweek'),
        ),
    ]
