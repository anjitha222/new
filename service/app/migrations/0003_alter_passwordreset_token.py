# Generated by Django 5.0.1 on 2024-05-20 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_message_mesage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='token',
            field=models.CharField(max_length=4),
        ),
    ]
