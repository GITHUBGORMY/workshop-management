# Generated by Django 4.1.7 on 2023-05-02 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshopApp', '0007_remove_feedback_user_feedback_worker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='worker',
            new_name='customer',
        ),
    ]