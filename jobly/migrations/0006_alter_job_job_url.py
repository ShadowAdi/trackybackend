# Generated by Django 5.1.2 on 2024-11-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobly', '0005_rename_job_url_job_job_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_url',
            field=models.URLField(),
        ),
    ]
