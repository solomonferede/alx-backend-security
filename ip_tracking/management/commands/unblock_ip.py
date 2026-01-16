from django.core.management.base import BaseCommand
from ip_tracking.models import BlockedIP


class Command(BaseCommand):
    help = "Unblock an IP address"

    def add_arguments(self, parser):
        parser.add_argument("ip_address", type=str, help="IP address to unblock")

    def handle(self, *args, **kwargs):
        ip = kwargs["ip_address"]

        deleted, _ = BlockedIP.objects.filter(ip_address=ip).delete()

        if deleted:
            self.stdout.write(
                self.style.SUCCESS(f"IP address {ip} has been unblocked.")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"IP address {ip} was not found.")
            )
