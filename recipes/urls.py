from django.urls import path, include
from recipes import views
from django.contrib.auth.views import LogoutView
from .form import LoginForm
from recipes.views import MyLoginView
urlpatterns = [
    path('accounts/login/', MyLoginView.as_view(),  name='login-in'),
    path('', views.home, name='home'),
    path('search', views.search_result, name='search'),
    path('add-movie', views.add_movie, name='add'),
    path('delete/<movie_name>/', views.delete_movie, name='delete'),
    path('accounts/logout/', LogoutView.as_view(),  name='logout'),

    # path('', include('django.contrib.auth.urls')),
    # path('login/', views.login_user, name='login'),
    # path('logout', views.logout_user, name='logout'),
]