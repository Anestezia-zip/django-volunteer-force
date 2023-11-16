# Generated by Django 4.2.6 on 2023-11-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_userprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Activist', 'Activist'), ('Volunteer', 'Volunteer'), ('Organization', 'Organization')], default='volunteer', max_length=20),
        ),
    ]
