# Generated by Django 4.2.6 on 2023-11-13 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_region_image4_alter_region_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='left_position',
        ),
        migrations.RemoveField(
            model_name='region',
            name='top_position',
        ),
    ]