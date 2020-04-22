from django.db import models


class Wallet(models.Model):
    name = models.CharField('имя кошелька', max_length=200)

    def __str__(self):
        return self.name

    # def view_txs(self):
    #     return self.objects.


class Transaction(models.Model):
    wallet_id = models.ForeignKey(Wallet, related_name='txs', on_delete=models.CASCADE)
    tx_comment = models.TextField('комментарий')
    tx_date = models.DateTimeField('дата транзакции')
    tx_sum = models.FloatField('сумма')

    def __str__(self):
        return str(self.tx_sum)
