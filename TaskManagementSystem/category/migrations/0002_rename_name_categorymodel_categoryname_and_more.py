# Generated by Django 4.2.7 on 2023-12-09 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='name',
            new_name='categoryName',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='categories',
            new_name='task',
        ),
    ]
