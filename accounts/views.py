"""
Authentication views for MainStage.

Handles user registration, login, logout, and admin dashboard.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import User
from .decorators import admin_only


@require_http_methods(["GET", "POST"])
def register(request):
    """
    User registration view.
    
    GET: Display registration form.
    POST: Create new user account and auto-login.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login after registration
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('core:home')
    else:
        form = RegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    User login view.
    
    GET: Display login form.
    POST: Authenticate user and start session.
    """
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('core:home')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required
@require_http_methods(["POST"])
def logout_view(request):
    """
    User logout view (POST only).
    
    Terminates user session and redirects to login page.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('accounts:login')


@admin_only
@require_http_methods(["GET"])
def dashboard(request):
    """
    Admin dashboard with user list.
    
    Shows all users, paginated (20 per page).
    Supports search by username or email.
    Filters by role (guest/admin).
    """
    users = User.objects.all().order_by('-date_joined')
    
    # Search by username or email
    search_query = request.GET.get('search', '').strip()
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    # Filter by role
    role_filter = request.GET.get('role', '').strip()
    if role_filter in ['guest', 'admin']:
        users = users.filter(role=role_filter)
    
    # Pagination: 20 users per page
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'role_filter': role_filter,
        'total_users': users.count(),
    }
    
    return render(request, 'accounts/dashboard.html', context)


@admin_only
@require_http_methods(["GET"])
def user_detail(request, user_id):
    """
    Admin user detail view.
    
    Shows user profile, role, account details.
    Provides buttons to promote, demote, or delete user.
    """
    user = get_object_or_404(User, id=user_id)
    
    # Prevent admin from editing themselves (safety check)
    is_self = user.id == request.user.id
    
    context = {
        'detail_user': user,  # Avoid template conflict with request.user
        'is_self': is_self,
    }
    
    return render(request, 'accounts/user_detail.html', context)


@admin_only
@require_http_methods(["POST"])
def promote_user(request, user_id):
    """
    Promote a guest user to admin.
    
    POST-only for security.
    Redirects back to user detail view.
    """
    user = get_object_or_404(User, id=user_id)
    
    # Prevent admin from promoting themselves (safety check)
    if user.id == request.user.id:
        messages.error(request, "You cannot promote yourself.")
        return redirect('accounts:user_detail', user_id=user.id)
    
    if user.role == 'guest':
        user.role = 'admin'
        user.save()
        messages.success(request, f"{user.username} has been promoted to Admin.")
    else:
        messages.info(request, f"{user.username} is already an Admin.")
    
    return redirect('accounts:user_detail', user_id=user.id)


@admin_only
@require_http_methods(["POST"])
def demote_user(request, user_id):
    """
    Demote an admin user to guest.
    
    POST-only for security.
    Redirects back to user detail view.
    """
    user = get_object_or_404(User, id=user_id)
    
    # Prevent admin from demoting themselves (safety check)
    if user.id == request.user.id:
        messages.error(request, "You cannot demote yourself.")
        return redirect('accounts:user_detail', user_id=user.id)
    
    if user.role == 'admin':
        user.role = 'guest'
        user.save()
        messages.success(request, f"{user.username} has been demoted to Guest.")
    else:
        messages.info(request, f"{user.username} is already a Guest.")
    
    return redirect('accounts:user_detail', user_id=user.id)


@admin_only
@require_http_methods(["GET", "POST"])
def delete_user(request, user_id):
    """
    Delete a user account (with confirmation).
    
    GET: Show deletion confirmation page.
    POST: Permanently delete the user.
    
    Prevents admin from deleting themselves.
    """
    user = get_object_or_404(User, id=user_id)
    
    # Prevent admin from deleting themselves
    if user.id == request.user.id:
        messages.error(request, "You cannot delete your own account.")
        return redirect('accounts:user_detail', user_id=user.id)
    
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f"User '{username}' has been permanently deleted.")
        return redirect('accounts:dashboard')
    
    # GET: Show confirmation page
    context = {'detail_user': user, 'is_self': False}
    return render(request, 'accounts/delete_user.html', context)
