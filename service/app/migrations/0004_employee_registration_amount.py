# Generated by Django 5.0.1 on 2024-05-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_passwordreset_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_registration',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
