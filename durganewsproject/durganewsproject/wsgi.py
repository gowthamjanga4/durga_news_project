"""
WSGI config for durganewsproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file.css, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'durganewsproject.settings')

application = get_wsgi_application()
