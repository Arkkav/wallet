from django.urls import path
from . import views


urlpatterns = [
    path('wallets/', views.index),
    path('wallets/create/', views.create_wallet),
    path('wallets/<str:wallet>/', views.index),
    path('wallets/<str:wallet>/update/', views.update_wallet),
    path('wallets/<str:wallet>/delete/', views.delete),

    path('wallets/<str:wallet>/txs/', views.txs),
    path('wallets/<str:wallet>/txs/create/', views.create_tx),
    path('wallets/<str:wallet>/txs/<str:tx>/', views.txs),
    path('wallets/<str:wallet>/txs/<str:tx>/update/', views.update_tx),
    path('wallets/<str:wallet>/txs/<str:tx>/delete/', views.delete),

    path('txs/', views.txs),
    path('txs/create/', views.create_tx),
    path('txs/<str:tx>/', views.txs),
    path('txs/<str:tx>/update/', views.update_tx),
    path('txs/<str:tx>/delete/', views.delete),
]