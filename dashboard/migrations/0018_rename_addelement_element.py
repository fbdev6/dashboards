# Generated by Django 4.1.2 on 2022-11-04 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_delete_followers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddElement',
            new_name='Element',
        ),
    ]