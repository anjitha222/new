# Generated by Django 5.0.1 on 2024-05-31 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_amountdetails_functions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='extra',
            new_name='day',
        ),
        migrations.RemoveField(
            model_name='amountdetails',
            name='functions',
        ),
    ]
