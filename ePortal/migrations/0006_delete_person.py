# Generated by Django 4.2.8 on 2024-01-11 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ePortal', '0005_person_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]