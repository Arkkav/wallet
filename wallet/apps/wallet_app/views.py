from .models import Transaction, Wallet
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
import json
from django.core.exceptions import ObjectDoesNotExist
import datetime



def index(request, wallet=None):
    # Format for GET URLs:
    # http://127.0.0.1:8000/wallet_app/wallets/5/
    # http://127.0.0.1:8000/wallet_app/wallets/
    if wallet is not None:
        try:
            wallets = Wallet.objects.filter(id=int(wallet)).annotate(balance=Sum('txs__tx_sum')).values()
            print(wallets)
        except ValueError:
            return HttpResponseForbidden("ID does not match format.")
    else:
        wallets = Wallet.objects.annotate(balance=Sum('txs__tx_sum')).values()

    for wal in wallets:
        if wal['balance'] is None:
            wal['balance'] = 0
    wallets = list(wallets)

    return JsonResponse(wallets, safe=False)


def txs(request, wallet=None, tx=None):
    # Format for GET URLs:
    # http://127.0.0.1:8000/wallet_app/txs/
    # http://127.0.0.1:8000/wallet_app/wallets/3/txs/
    # http://127.0.0.1:8000/wallet_app/wallets/3/txs/3/
    # http://127.0.0.1:8000/wallet_app/txs/3/

    if tx is not None:
        try:
            trancs = list(Transaction.objects.filter(id=int(tx)).values())
        except ValueError:
            return HttpResponseForbidden("ID does not match format.")
    elif wallet is not None:
        try:
            trancs = list(Transaction.objects.filter(wallet_id=int(wallet)).values())
        except ValueError:
            return HttpResponseForbidden("ID does not match format.")
    else:
        trancs = list(Transaction.objects.values())

    return JsonResponse(trancs, safe=False)


@csrf_exempt
def create_wallet(request):
    # {"name": "wal5"} - format in POST body
    # http://127.0.0.1:8000/wallet_app/wallets/create/

    try:
        post_dict = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseForbidden("Inappropriate JSON  format.")

    try:
        name = post_dict.get('name', None)
    except ValueError:
        return HttpResponseForbidden("Wallet name does not match format.")

    if name is None:
        return HttpResponseForbidden("Inappropriate format.")
    a = Wallet(name=name)
    a.save()
    return HttpResponse('Wallet {} has been created.'.format(name))


@csrf_exempt
def update_wallet(request, wallet=None):
    # {"name": "my_wal2134297"} - format in PUT body
    # http://127.0.0.1:8000/wallet_app/wallets/1/update/

    try:
        post_dict = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseForbidden("Inappropriate JSON  format.")

    if wallet is None:
        return HttpResponseForbidden("There is no wallet ID to update.")

    try:
        a = Wallet.objects.get(id=int(wallet))
    except ObjectDoesNotExist:
        return HttpResponseForbidden("There is no wallets with this ID.".format(str(wallet)))
    except ValueError:
        return HttpResponseForbidden("ID does not match format.")

    try:
        new_name = post_dict.get('name', None)
    except ValueError:
        return HttpResponseForbidden("Wallet name does not match format.")
    if new_name is None:
        return HttpResponseForbidden('There is no new name for the wallet.')
    old_name = a.name
    a.name = new_name
    a.save()
    return HttpResponse('Wallet name {} has been changed to {}.'.format(old_name, new_name))


@csrf_exempt
def create_tx(request, wallet=None):
    # {"wallet_id": 2, "tx_comment": "ergergweg", "tx_date": "2020-04-20 07:26:33", "tx_sum": 800} - format in POST body
    # {"tx_comment": "ergergweg", "tx_date": "2020-04-20 07:26:33", "tx_sum": 800} - format in POST body
    #       with URLs http://127.0.0.1:8000/wallet_app/txs/create/
    #                 http://127.0.0.1:8000/wallet_app/wallets/3/txs/create/


    try:
        post_dict = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseForbidden("Inappropriate JSON  format.")

    if wallet is not None:
        try:
            wallet_id = int(wallet)
        except ValueError:
            return HttpResponseForbidden("ID does not match format.")
    else:
        try:
            wallet_id = post_dict.get('wallet_id', None)
        except ValueError:
            return HttpResponseForbidden("Transaction ID does not match format.")

    try:
        a = Wallet.objects.get(id=wallet_id)
    except ObjectDoesNotExist:
        return HttpResponseForbidden("There is no wallets with this ID or no wallet ID has been received.".format(str(wallet_id)))

    tx_comment = post_dict.get('tx_comment', None)
    if tx_comment is None:
        return HttpResponseForbidden("Inappropriate format.")

    tx_date = post_dict.get('tx_date', None)
    if tx_date is None:
        return HttpResponseForbidden("Inappropriate format.")
    try:
        tx_date = datetime.datetime.strptime(post_dict.get('tx_date', None), '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return HttpResponseForbidden("Time data does not match format.")

    tx_sum = post_dict.get('tx_sum', None)
    if tx_sum is None:
        return HttpResponseForbidden("Inappropriate format.")
    try:
        tx_sum = float(post_dict.get('tx_sum', None))
    except ValueError:
        return HttpResponseForbidden("Sum does not match format.")
    if tx_sum is None:
        return HttpResponseForbidden("Inappropriate format.")

    b = a.txs.create(wallet_id=wallet_id, tx_comment=tx_comment, tx_date=tx_date, tx_sum=tx_sum)
    return HttpResponse('Transaction ID {} has been created.'.format(str(b.id)))



@csrf_exempt
def update_tx(request, tx=None):
    # {"wallet_id": 2, "tx_comment": "ergergweg", "tx_date": "2020-04-20 07:26:33", "tx_sum": 800} - format in PUT body
    #       with URLs http://127.0.0.1:8000/wallet_app/txs/2/update/
    #                 http://127.0.0.1:8000/wallet_app/wallets/3/txs/2/udpate/

    try:
        post_dict = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseForbidden("Inappropriate JSON  format.")

    try:
        tx_id = int(tx)
    except ValueError:
        return HttpResponseForbidden("Transaction ID does not match format.")
    try:
        a = Transaction.objects.get(id=tx_id)
    except ObjectDoesNotExist:
        return HttpResponseForbidden("There is no transaction with this ID or no transaction ID has been received.".format(str(tx_id)))


    wallet_id = post_dict.get('wallet_id', None)
    if wallet_id is None:
        return HttpResponseForbidden("Inappropriate format.")
    try:
        wallet_id = int(wallet_id)
    except ValueError:
        return HttpResponseForbidden("Wallet ID does not match format.")
    try:
        b = Wallet.objects.get(id=wallet_id)
    except ObjectDoesNotExist:
        return HttpResponseForbidden("There is no wallets with this ID or no wallet ID has been received.".format(str(wallet_id)))
    tx_comment = post_dict.get('tx_comment', None)
    if tx_comment is None:
        return HttpResponseForbidden("Inappropriate format.")


    tx_date = post_dict.get('tx_date', None)
    if tx_date is None:
        return HttpResponseForbidden("Inappropriate format.")
    try:
        tx_date = datetime.datetime.strptime(post_dict.get('tx_date', None), '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return HttpResponseForbidden("Time data does not match format.")

    tx_sum = post_dict.get('tx_sum', None)
    if tx_sum is None:
        return HttpResponseForbidden("Inappropriate format.")
    try:
        tx_sum = float(tx_sum)
    except ValueError:
        return HttpResponseForbidden("Sum does not match format.")

    a.wallet_id = b
    a.tx_comment = tx_comment
    a.tx_date = tx_date
    a.tx_sum = tx_sum
    a.save()
    return HttpResponse('Transaction {} has been changed.'.format(str(tx_id)))


@csrf_exempt
def delete(request, wallet=None, tx=None):
    # Format for DELETE URLs:
    # http://127.0.0.1:8000/wallet_app/txs/3/delete/
    # http://127.0.0.1:8000/wallet_app/wallets/2/delete/
    # http://127.0.0.1:8000/wallet_app/wallets/2/txs/3/delete/
    if tx is not None:
        try:
         a = Transaction.objects.get(id=int(tx))
        except ValueError:
            return HttpResponseForbidden("ID does not match format.")
        except ObjectDoesNotExist:
            return HttpResponseForbidden(
                "There is no transaction with this ID or no transaction ID has been received.".format(str(tx)))
        if not a:
            HttpResponseForbidden('There is no transactions with ID {}.'.format(str(tx)))
        a.delete()
        return HttpResponse('Wallet with ID {} has been deleted.'.format(str(tx)))
    elif wallet is not None:
        try:
            a = Wallet.objects.get(id=int(wallet))
        except ValueError:
            return HttpResponseForbidden("ID does not match format.")
        except ObjectDoesNotExist:
            return HttpResponseForbidden("There is no wallet with this ID or no wallet ID has been received.".format(str(tx)))
        if not a:
            HttpResponseForbidden('There is no wallet with ID {}.'.format(str(wallet)))
        a.delete()
        return HttpResponse('Wallet with ID {} has been deleted/'.format(str(wallet)))
    else:
        HttpResponseForbidden('There is no IDs received.')
