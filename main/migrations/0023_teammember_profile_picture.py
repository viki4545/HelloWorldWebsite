# Generated by Django 2.2.2 on 2019-08-11 17:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20190811_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
