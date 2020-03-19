from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.conf import settings
from django.core.mail import send_mail

from .forms import RegForm
from django.http import HttpResponse, Http404
from django.contrib import messages

# Create your views here.
def register(request):
  if request.method=='POST':
    # if this is a POST request we need to process the form data
    form = RegForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_active = False
      user.save()
      site = get_current_site(request)
      mail_subject = "Confirm Registration"
      message = render_to_string('acc_active_email.html', {
        'user': user,
        'domain': site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
      })
      to_email = form.cleaned_data.get('email')
      from_email = settings.EMAIL_HOST_USER
      to_list=[to_email]
      send_mail(mail_subject, message, from_email, to_list)
      messages.success(request, 'A Confirmation link was sent. Confirm your Account to Login!')
      return redirect('/users/login')

  else:
    form = RegForm()
  return render(request, 'register.html', {'form': form})



def signin(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']

    user= auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Invalid Credentials')

  else:
    return render(request, 'login.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')