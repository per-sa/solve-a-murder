from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *



urlpatterns = [
    # pages
    path('', home, name='home'),
    path('victims/', victims, name='victims'),

    # auth
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', signup, name='register'),
    path('profile/', editprofile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
