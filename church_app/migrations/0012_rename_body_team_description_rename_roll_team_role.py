# Generated by Django 5.1.6 on 2025-03-14 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0011_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='body',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='roll',
            new_name='role',
        ),
    ]
