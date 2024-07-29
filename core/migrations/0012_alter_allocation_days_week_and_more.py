# Generated by Django 5.0.6 on 2024-07-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_allocation_days_week_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='days_week',
            field=models.CharField(choices=[('SEG', 'Segunda-feira'), ('TER', 'Terça-feira'), ('QUA', 'Quarta-feira'), ('QUI', 'Quinta-feira'), ('SEX', 'Sexta-feira'), ('SAB', 'Sábado')], max_length=3),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='timetable',
            field=models.CharField(choices=[('08:00', '08:00 - 09:00'), ('09:00', '09:00 - 10:00'), ('10:00', '10:00 - 11:00'), ('11:00', '11:00 - 12:00'), ('12:00', '12:00 - 13:00'), ('13:00', '13:00 - 14:00'), ('14:00', '14:00 - 15:00'), ('15:00', '15:00 - 16:00'), ('16:00', '16:00 - 17:00'), ('17:00', '17:00 - 18:00'), ('18:00', '18:00 - 19:00'), ('19:00', '19:00 - 20:00'), ('20:00', '20:00 - 21:00'), ('21:00', '21:00 - 22:00')], max_length=5),
        ),
    ]
