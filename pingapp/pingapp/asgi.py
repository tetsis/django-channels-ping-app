"""
ASGI config for pingapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import private.routing
import public.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingapp.settings')
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            private.routing.websocket_urlpatterns +
            public.routing.websocket_urlpatterns
        )
    ),
})