# Generated by Django 5.0.3 on 2024-04-15 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_answer_module_notes_question_user_user_module_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='moduleID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='module_notes', to='main.module'),
            preserve_default=False,
        ),
    ]
