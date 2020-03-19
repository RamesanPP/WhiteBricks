
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('search', views.search, name='search'),
path('addpg', views.insert_pg, name='addpg'),
path('profile', views.profile, name='profile'),
path('logout', auth_views.LogoutView.as_view(), name='logout'),
]