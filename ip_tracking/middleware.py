from django.http import HttpResponseForbidden
from django.utils import timezone
from django.core.cache import cache
from .models import RequestLog


class IPTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        cache_key = f"blocked_ip:{ip}"

        # Redis-based block check
        if cache.get(cache_key):
            return HttpResponseForbidden("Your IP has been temporarily blocked.")

        # Log allowed requests
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path,
            timestamp=timezone.now()
        )

        return self.get_response(request)

    def get_client_ip(self, request):
        xff = request.META.get("HTTP_X_FORWARDED_FOR")
        return xff.split(",")[0] if xff else request.META.get("REMOTE_ADDR")
