# Generated by Django 5.0.1 on 2024-05-24 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_payment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]