# Generated by Django 5.0.3 on 2024-10-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_description_task_task_remove_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.TextField(default='taskName'),
        ),
    ]
