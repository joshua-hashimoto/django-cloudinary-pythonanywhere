# Generated by Django 3.2 on 2022-09-19 12:02

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_snap_snap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snap',
            name='snap',
            field=models.ImageField(upload_to=website.models.upload_image_to),
        ),
    ]
