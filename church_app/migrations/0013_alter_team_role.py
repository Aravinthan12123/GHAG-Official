# Generated by Django 5.1.6 on 2025-03-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0012_rename_body_team_description_rename_roll_team_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='role',
            field=models.CharField(max_length=50),
        ),
    ]
