# Generated by Django 4.2.8 on 2024-01-11 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ePortal', '0004_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.CharField(default='none', max_length=30),
        ),
    ]