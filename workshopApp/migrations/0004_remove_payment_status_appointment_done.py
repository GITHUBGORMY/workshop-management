# Generated by Django 4.1.7 on 2023-04-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshopApp', '0003_alter_appointment_schedule_alter_schedule_worker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.AddField(
            model_name='appointment',
            name='done',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
