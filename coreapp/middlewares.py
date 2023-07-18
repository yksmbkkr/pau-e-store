from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse


def profile_check_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated and not request.user.is_superuser and not request.user.is_profile_complete and not reverse(
                'customer:profile-update') in request.path and not reverse(
                'customer:logout') in request.path and not reverse('coreapp:app-logout') in request.path:
            if '/browser-auth/' in request.path:
                return JsonResponse({
                    'alreadyLoggedIn': True,
                    'next': 'customer:profile-update'
                })
            messages.warning(request, "Please tell us more about you.")
            return redirect(reverse('customer:profile-update'))
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
