"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

import traceback

from inspect import istraceback

from django.core.serializers.json import DjangoJSONEncoder


class JSONEncoder(DjangoJSONEncoder):
    """A custom Encoder extending the DjangoJSONEncoder."""

    def default(self, o):
        if istraceback(o):
            return "".join(traceback.format_tb(o)).strip()

        if isinstance(o, (Exception, type)):
            return str(o)

        try:
            return super(DjangoJSONEncoder, self).default(o)
        except TypeError:
            try:
                return str(o)
            except Exception:
                return None


encoder = JSONEncoder(
    indent=4,
    sort_keys=True)
