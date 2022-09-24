from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # pages
    path('', home, name='home'),
    path('victims/', victims, name='victims'),

    # auth
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
