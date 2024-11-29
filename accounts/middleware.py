from datetime import datetime
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages

class SessionExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_expiry = request.session.get('expiry_time', None)

        if session_expiry:
            session_expiry = datetime.fromisoformat(session_expiry)

            if timezone.now() > session_expiry:
                messages.error(request, "Your session has expired. Please log in again.")
                del request.session['expiry_time']
                return redirect('login')

        response = self.get_response(request)
        return response
