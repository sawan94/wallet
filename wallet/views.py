# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from wallet.models import Wallet,Transaction
from wallet.serializers import walletSerializer,TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime

class WalletList(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = walletSerializer
    
    def get_queryset(self):
        wallets =  Wallet.objects.filter(owner=self.request.user,is_active=True).order_by("-added_on")
        return wallets

class CreateWallet(generics.CreateAPIView):
    serializer_class = walletSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CreateTransaction(APIView):
    
    def post(self, request, *args, **kwargs):
        wallet_id = kwargs["wallet_id"]
        transaction_type = int(request.POST.get("transaction_type"))
        wallet = get_object_or_404(Wallet,pk=wallet_id)
        if not wallet.owner == request.user:
            return Response({
                "message":"You do not own this wallet",
                "status":False
            })
        amount = int(self.request.POST.get("amount"))
        if transaction_type == 2 and (wallet.get_wallet_balance()-amount) <= (-50000) :
            return Response({
                "message":"Wallet Transaction could not be completed.Limit Reached.",
                "status":False
            })
        transaction = Transaction.objects.create(
            wallet = wallet,
            transaction_type = transaction_type, 
            status = Transaction.COMPLETED,
            amount = amount,
            completed_at = datetime.now()
        )
        return Response({
            "message":"Transaction Succesfull, New Wallet Balance: " + str(wallet.get_wallet_balance()),
            "transactionId": transaction.get_transaction_id()
        })

class CancelTransaction(APIView):
    def delete(self, request, *args, **kwargs):
        wallet_id = kwargs["wallet_id"]
        transaction_id = kwargs["transaction_id"].replace("MPAANI_","")
        transaction = get_object_or_404(Transaction,pk=transaction_id)
        wallet = get_object_or_404(Wallet,pk=wallet_id)
        if not transaction.wallet == wallet:
            return Response({
                "message":"Transaction does not exist in this wallet",
            })
        transaction.transaction_type = Transaction.CANCELLED
        transaction.cancelled_at = datetime.now()
        transaction.save()
        return Response({
            "message":"Transaction Cancelled Succesfully, New Wallet Balance: " + str(wallet.get_wallet_balance()),
            "transactionId": transaction.get_transaction_id()
        })

class ViewPassbook(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        wallet_id = self.kwargs["wallet_id"]
        user_id = self.kwargs["user_id"]
        return Transaction.objects.filter(wallet_id=wallet_id).order_by("-initiated_at")