# Generated by Django 5.0.1 on 2024-05-24 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_card_no_payment_advamount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='advAmount',
            new_name='advAmound',
        ),
    ]
