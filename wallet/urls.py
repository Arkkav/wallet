"""wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallet_app/', include('wallet_app.urls')),
    path('wallet_app/wallets/', include('wallet_app.urls')),
    path('wallet_app/wallets/create/', include('wallet_app.urls')),
    path('wallet_app/wallets/<str:wallet>/', include('wallet_app.urls')),
    path('wallet_app/wallets/<str:wallet>/update/', include('wallet_app.urls')),
    path('wallet_app/wallets/<str:wallet>/delete/', include('wallet_app.urls')),

    path('wallet_app/wallets/<str:wallet>/txs/', include('wallet_app.urls')),
    path('wallet_app/wallets/<str:wallet>/txs/create/', include('wallet_app.urls')),
    path('wallet_app/wallets/<str:wallet>/txs/<str:tx>/', include('wallet_app.urls')),
    path('wallet_app/wallets/<str:wallet>/txs/<str:tx>/update/', include('wallet_app.urls')),
    path('wallet_app/wallets/<str:wallet>/txs/<str:tx>/delete/', include('wallet_app.urls')),

    path('wallet_app/txs/', include('wallet_app.urls')),
    path('wallet_app/txs/create/', include('wallet_app.urls')),
    path('wallet_app/txs/<str:tx>/', include('wallet_app.urls')),
    path('wallet_app/txs/<str:tx>/update/', include('wallet_app.urls')),
    path('wallet_app/txs/<str:tx>/delete/', include('wallet_app.urls')),


]
