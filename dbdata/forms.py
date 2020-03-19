from django import forms

from . import models


class PGForm(forms.Form):
    pg_name = forms.CharField(label='PG Name')  
    pg_type = forms.CharField(label='PG Type', required=False)
    pg_hc = forms.IntegerField(label='HeadCount')
    pg_city = forms.CharField(label='City')
    pg_img = forms.ImageField(label='Image')
    pg_rent = forms.IntegerField(label='Rent')
    pg_deposit = forms.IntegerField(label='Deposit')
    pg_desc = forms.CharField(widget=forms.Textarea, label='Description', required=False)  
