# Generated by Django 4.1 on 2022-09-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_rename_body_comment_message_remove_comment_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='dahboard',
            field=models.CharField(max_length=200, verbose_name='Dashboard username'),
        ),
    ]