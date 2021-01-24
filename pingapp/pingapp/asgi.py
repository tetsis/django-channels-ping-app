"""
ASGI config for pingapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import private.routing
import public.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pingapp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            private.routing.websocket_urlpatterns +
            public.routing.websocket_urlpatterns
        )
    ),
})