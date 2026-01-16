# alx-backend-security — IP Tracking

## Summary

Django app to log requests, blacklist IPs, enrich logs with geolocation, apply rate limits, and flag suspicious IPs via a Celery task.

## Requirements

- Python 3.8+
- Django
- Redis (for caching/rate limiting/Celery broker)
- Celery
- django-ipgeolocation
- django-ratelimit

## Quick setup

1. Clone repo
2. Create venv and install:
   pip install -r requirements.txt
3. Add `ip_tracking` to INSTALLED_APPS and register middleware in settings.py.
4. Configure Redis URL and celery settings in settings.py.
5. Run migrations:
   python manage.py migrate
6. Create superuser (optional):
   python manage.py createsuperuser
7. Start services:
   - Django: python manage.py runserver
   - Celery worker: celery -A project_name worker -l info
   - Celery beat (for hourly task): celery -A project_name beat -l info

## Useful commands

- Block an IP: python manage.py block_ip <ip_address>
- Run tests: python manage.py test
- Manual QA: request a review when done (per project instructions)

## Tasks implemented

- Task 0: IP logging middleware + RequestLog model
- Task 1: BlockedIP model, middleware blocks listed IPs, management command
- Task 2: Geolocation enrichment (country, city) with caching
- Task 3: Rate limiting (django-ratelimit) configured for auth/anon
- Task 4: Hourly Celery task to flag SuspiciousIP model

## Notes

- Anonymize/truncate IPs to meet privacy requirements and set retention policy.

License: ALX © 2026
