# Generated by Django 4.2.7 on 2023-12-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_remove_categorymodel_task'),
        ('task', '0003_alter_taskmodel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='task',
            field=models.ManyToManyField(to='category.categorymodel'),
        ),
    ]
