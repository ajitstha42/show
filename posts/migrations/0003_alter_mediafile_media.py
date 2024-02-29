# Generated by Django 5.0 on 2024-02-29 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='media',
            field=models.FileField(upload_to='media_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'mp4', 'mkv'])]),
        ),
    ]