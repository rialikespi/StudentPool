# Generated by Django 5.0.3 on 2024-04-11 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_module_user_remove_rating_answerid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_module',
            name='module_code',
        ),
        migrations.RemoveField(
            model_name='user_module',
            name='user',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='User_Module',
        ),
    ]