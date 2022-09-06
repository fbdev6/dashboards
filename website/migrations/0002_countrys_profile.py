# Generated by Django 4.1 on 2022-08-30 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countrys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=70)),
                ('premium_bio', models.CharField(max_length=140)),
                ('mobile_number', models.IntegerField(default=998)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.countrys')),
            ],
        ),
    ]