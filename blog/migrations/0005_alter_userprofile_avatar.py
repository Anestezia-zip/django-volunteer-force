# Generated by Django 4.2.6 on 2023-11-29 10:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dyadwedsy/image/upload/v1700328631/volunteer/anonym_nplen6.png', max_length=255, verbose_name='image'),
        ),
    ]
