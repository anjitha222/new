# Generated by Django 5.0.1 on 2024-05-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_amountdetails_remove_employee_registration_advamound_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_registration',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]