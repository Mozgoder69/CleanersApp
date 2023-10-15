""" Exposes the WSGI callable as a module-level variable ``application``.
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/ """

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "general.settings")

application = get_wsgi_application()
