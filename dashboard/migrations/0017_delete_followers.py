# Generated by Django 4.1.2 on 2022-11-04 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_followers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Followers',
        ),
    ]