# Generated by Django 5.0.1 on 2024-05-24 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_advamount_payment_advamound'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
