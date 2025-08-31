import threading
from audioop import reverse

from django.shortcuts import redirect

_thread_locals = threading.local()


class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.user = request.user
        response = self.get_response(request)
        _thread_locals.user = None
        return response

