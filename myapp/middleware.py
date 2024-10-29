from django.utils.deprecation import MiddlewareMixin
from django.db import close_old_connections


class DBConnectionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        close_old_connections()

    def process_response(self, request, response):
        close_old_connections()
        return response
