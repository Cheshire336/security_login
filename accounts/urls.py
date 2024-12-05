from django.urls import path
from . import views
from .views import request_evaluation
from django.shortcuts import render
from .views import evaluation_list, home_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('evaluation/', request_evaluation, name='request_evaluation'),
    path('evaluation/success/', lambda request: render(request, 'accounts/evaluation_success.html'), name='evaluation_success'),
    path('evaluation/list/', evaluation_list, name='evaluation_list'),
    path('safe-query/', views.safe_query, name='safe_query'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
