# Generated by Django 3.2 on 2022-09-19 11:59

import cloudinary_storage.storage
from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20220919_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snap',
            name='snap',
            field=models.ImageField(storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to=website.models.upload_image_to),
        ),
    ]
