# Generated by Django 4.2.6 on 2023-11-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Activist', 'Activist'), ('Volunteer', 'Volunteer'), ('Organization', 'Organization')], default='Volunteer', max_length=20),
        ),
    ]
