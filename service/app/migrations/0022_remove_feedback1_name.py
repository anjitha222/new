# Generated by Django 5.0.1 on 2024-05-30 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_feedback1_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback1',
            name='name',
        ),
    ]
