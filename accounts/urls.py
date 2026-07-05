"""
URL configuration for the accounts app.

Routes for registration, login, logout, and admin dashboard.
Uses 'accounts' namespace for reverse URL lookups.
"""

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Auth routes
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Admin dashboard routes
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/<int:user_id>/promote/', views.promote_user, name='promote_user'),
    path('user/<int:user_id>/demote/', views.demote_user, name='demote_user'),
    path('user/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]
