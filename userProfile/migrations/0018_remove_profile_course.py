# Generated by Django 5.0.3 on 2024-04-18 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0017_remove_profile_module1_remove_profile_module2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='course',
        ),
    ]
