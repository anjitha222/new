# Generated by Django 5.0.1 on 2024-05-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_user_passwordreset_user_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_registration',
            old_name='amount',
            new_name='advAmound',
        ),
        migrations.AddField(
            model_name='employee_registration',
            name='fullamount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]