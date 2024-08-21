"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

from decouple import config

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from .base import *


# -----------------------------------------------------------------------------
# --- Override Settings here.
# -----------------------------------------------------------------------------
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE":   "django.db.backends.postgresql",
        "NAME":     config("DB_NAME", "ws_demo"),
        "USER":     config("DB_USER", "ws_demo"),
        "PASSWORD": config("DB_PASSWORD", "ws_demo"),
        "HOST":     config("DB_HOST", "db"),
        "PORT":     config("DB_PORT", 5432),
    }
}

###############################################################################
### ASGI / WEBSOCKET                                                        ###
###############################################################################
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
            "symmetric_encryption_keys": [SECRET_KEY, ],
        },
    },
}
