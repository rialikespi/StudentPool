# Generated by Django 5.0.3 on 2024-04-18 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0016_remove_profile_friends_delete_friendrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='module1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='module2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='module3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='module4',
        ),
    ]
