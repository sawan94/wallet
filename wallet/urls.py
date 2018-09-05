from django.conf.urls import url
from wallet.views import *

urlpatterns = [
        url(r"^user/(?P<user_id>[0-9]+)/wallet/$",WalletList.as_view(),name="wallet_list"),
        url(r"^user/(?P<user_id>[0-9]+)/wallet/create/$",CreateWallet.as_view(),name="wallet_create"),
        url(r"^user/(?P<user_id>[0-9]+)/wallet/(?P<wallet_id>[0-9]+)/transaction/$",CreateTransaction.as_view(),name="transaction_create"),
        url(r"^user/(?P<user_id>[0-9]+)/wallet/(?P<wallet_id>[0-9]+)/transaction/(?P<transaction_id>[a-zA-Z0-9\-_.&]+)/$",CancelTransaction.as_view(),name="transaction_cancel"),
        url(r"^user/(?P<user_id>[0-9]+)/wallet/(?P<wallet_id>[0-9]+)/$",ViewPassbook.as_view(),name="passbook"),
]