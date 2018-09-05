# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models import Sum

# Create your models here.
class Wallet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(_('active'), default=True)
    added_on = models.DateTimeField(_('added_on'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('wallet')
        verbose_name_plural = _('wallets')

    def get_wallet_balance(self):
        credit = self.transaction_set.filter(status=Transaction.COMPLETED,transaction_type = Transaction.CREDIT)
        debit  = self.transaction_set.filter(status=Transaction.COMPLETED,transaction_type = Transaction.DEBIT)
        credit_balance = credit.aggregate(Sum('amount'))
        debit_balance  = debit.aggregate(Sum('amount'))
        return (credit_balance["amount__sum"]or 0) - (debit_balance["amount__sum"] or 0)

    def get_wallet_id(self):
        '''
        Returns the wallet name wrt to ID.
        '''
        full_name = '%s_%s' % ("MPAANI_WALLET", self.id)
        return full_name.strip()

class Transaction(models.Model):
    CREDIT = 1
    DEBIT = 2
    TRANS_CHOICES =(
        (CREDIT,'Credit'),
        (DEBIT,'Debit')
        )
    INITITATED = 1
    COMPLETED = 2 
    FAILED = 3
    CANCELLED = 4
    STATUS_CHOICES = (
        (INITITATED,'Inititated'),
        (COMPLETED,'Completed'),
        (FAILED,'Failed'),
        (CANCELLED,'Cancelled')
    )

    wallet = models.ForeignKey(Wallet)
    transaction_type =  models.SmallIntegerField(choices=TRANS_CHOICES)
    status =  models.SmallIntegerField(choices=STATUS_CHOICES,default=INITITATED)
    amount = models.IntegerField(default=0)
    initiated_at = models.DateTimeField(_('initiated_at'), auto_now_add=True)
    completed_at = models.DateTimeField(_('completed_at'), null=True,blank=True)
    cancelled_at = models.DateTimeField(_('cancelled_at'), null=True,blank=True)
        
    def get_transaction_id(self):
        '''
        Returns the wallet name wrt to ID.
        '''
        full_name = '%s_%s' % ("MPAANI", self.id)
        return full_name.strip()
