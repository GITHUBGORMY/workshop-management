# Generated by Django 4.1.7 on 2023-04-28 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshopApp', '0004_remove_payment_status_appointment_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='appoint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workshopApp.appointment'),
        ),
    ]
