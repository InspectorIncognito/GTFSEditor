# Generated by Django 3.1.3 on 2020-11-19 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0015_project_gtfs_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='last_modification',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]