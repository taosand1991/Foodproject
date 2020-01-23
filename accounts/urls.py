from django.urls import path, include
from accounts import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
    path('update', views.user_edit, name='update')
    # path('change-password', views.change_password, name='password'),
]