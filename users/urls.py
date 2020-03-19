from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('register', views.register, name='register'),
path('login', auth_views.LoginView.as_view(template_name ='login.html'), name='login'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]

app_name='users'