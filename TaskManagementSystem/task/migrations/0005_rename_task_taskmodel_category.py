# Generated by Django 4.2.7 on 2023-12-10 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_taskmodel_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmodel',
            old_name='task',
            new_name='category',
        ),
    ]
