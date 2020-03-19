# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['whitebricksinc.pg@gmail.com'])
                messages.success(request, 'We have recieved your mail and will be in touch soon!')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/pgfinder/#contact')
    return render(request, "index.html", {'form': form})



