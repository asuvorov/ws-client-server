"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

import os
import django

from channels.routing import get_default_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

django.setup()


channel_layer = get_default_application()
