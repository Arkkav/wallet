# Generated by Django 3.0.5 on 2020-04-20 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='wallet_name',
            new_name='wallet_id',
        ),
    ]
