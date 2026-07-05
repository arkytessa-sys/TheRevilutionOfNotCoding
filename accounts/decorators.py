"""
Access control decorators for MainStage.

Provides @admin_only decorator to restrict views to admin users.
"""

from functools import wraps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse


def admin_only(view_func):
    """
    Decorator to restrict view access to admin users only.
    
    Requires user to be logged in (via @login_required) and have role='admin'.
    Non-admin users are redirected to home page with a 403 Forbidden message.
    """
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        # Check if user is admin
        if request.user.role != 'admin':
            # Return 403 Forbidden for attempted access
            return HttpResponseForbidden(
                "You do not have permission to access this page."
            )
        return view_func(request, *args, **kwargs)
    return wrapper
