from django.contrib import admin
from django.urls import path, include
from ePortal.views import test_index, test_profile, test_form
from django.contrib.auth import views as auth_views
from ePortal.models import Notification
from ePortal.views import get_notifications

urlpatterns = [
    path("index/", test_index),
    path("login/", auth_views.LoginView.as_view(), name = 'login'),
    path("logout/", auth_views.LogoutView.as_view(), name ='logout'),
    path("admin/", admin.site.urls),
    path("profile/", test_profile, name = 'profile'),
    path('get-notifications/', get_notifications, name='get_notifications'),
    path("form/", test_form, name = 'form')
]
