# Generated by Django 3.0.5 on 2020-04-20 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='имя кошелька')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx_comment', models.TextField(verbose_name='комментарий')),
                ('tx_date', models.DateTimeField(verbose_name='дата транзакции')),
                ('tx_sum', models.FloatField(verbose_name='сумма')),
                ('wallet_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='txs', to='wallet_app.Wallet')),
            ],
        ),
    ]
