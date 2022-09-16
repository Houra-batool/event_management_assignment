from django.urls import path, include
from knox import views as knox_views

from . views import *



urlpatterns = [
    path('auth/', include('knox.urls')),   
    path('register', SignUpAPI.as_view()),
    path('login', SignInAPI.as_view()),
    path('user', MainUser.as_view()),
    path('logout',knox_views.LogoutView.as_view(), name="knox-logout"),]
