# Generated by Django 5.1.6 on 2025-03-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0015_alter_team_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
