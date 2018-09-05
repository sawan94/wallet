from users.models import User
from wallet.models import Wallet,Transaction
from rest_framework import serializers

class walletSerializer(serializers.HyperlinkedModelSerializer):
    walletId = serializers.CharField(source='get_wallet_id', read_only=True)
    class Meta:
        model = Wallet
        fields = ('name', 'walletId','added_on')


class TransactionSerializer(serializers.ModelSerializer):
    transactionId = serializers.CharField(source='get_transaction_id', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    transaction_type = serializers.CharField(source='get_transaction_type_display', read_only=True)
    class Meta:
        model = Transaction
        fields = ('transactionId','status','transaction_type','amount','initiated_at','completed_at','cancelled_at',)