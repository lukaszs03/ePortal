# Generated by Django 4.2.8 on 2024-01-05 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ePortal', '0002_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='message',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='created_at',
            new_name='timestamp',
        ),
    ]
