from django.core.management.base import BaseCommand
from django.core.cache import cache
from ip_tracking.models import BlockedIP


class Command(BaseCommand):
    help = "Block an IP address using Redis"

    def add_arguments(self, parser):
        parser.add_argument("ip_address", type=str)
        parser.add_argument(
            "--timeout",
            type=int,
            default=3600,
            help="Block duration in seconds (default: 1 hour)"
        )

    def handle(self, *args, **kwargs):
        ip = kwargs["ip_address"]
        timeout = kwargs["timeout"]

        # Save in DB (audit)
        BlockedIP.objects.get_or_create(ip_address=ip)

        # Save in Redis (enforcement)
        cache.set(f"blocked_ip:{ip}", 1, timeout=timeout)

        self.stdout.write(
            self.style.SUCCESS(
                f"IP {ip} blocked for {timeout} seconds."
            )
        )
