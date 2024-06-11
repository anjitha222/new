# Generated by Django 5.0.1 on 2024-05-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_amount_employee_registration_advamound_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_registration',
            name='advAmound',
        ),
        migrations.RemoveField(
            model_name='employee_registration',
            name='fullamount',
        ),
        migrations.RemoveField(
            model_name='employee_registration',
            name='specialised_skill',
        ),
        migrations.AddField(
            model_name='emp_gallery',
            name='advAmound',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp_gallery',
            name='fullamount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp_gallery',
            name='specialised_skill',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
