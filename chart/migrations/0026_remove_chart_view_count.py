# Generated by Django 4.1.2 on 2022-11-24 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0025_myuser_email_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='view_count',
        ),
    ]
