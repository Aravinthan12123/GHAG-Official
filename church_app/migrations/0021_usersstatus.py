# Generated by Django 5.1.6 on 2025-03-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0020_churchmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usersstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
        ),
    ]
