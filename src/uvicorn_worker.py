"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

from decouple import config
from uvicorn.workers import UvicornWorker

try:
    import os
    import uvloop

    class Worker(UvicornWorker):
        """
        In order to run under `gunicorn`, we want to be able to force `uvloop`, and configure
        `ws_ping`, if needed.

        NOTE: We'd call `gunicorn` as:

        gunicorn asgi:channel_layer --worker-class uvicorn_worker.Worker --reload
        """

        ws_ping_interval = config("WS_PING_INTERVAL", 20.0, cast=float)
        ws_ping_timeout = config("WS_PING_TIMEOUT", 20.0, cast=float)

        CONFIG_KWARGS = {
            "loop":             "uvloop",
            "http":             "auto",
            "proxy_headers":    True,
            "ws_ping_interval": ws_ping_interval,
            "ws_ping_timeout":  ws_ping_timeout,
            "use_colors":       True,
        }

except ImportError:
    Worker = UvicornWorker
