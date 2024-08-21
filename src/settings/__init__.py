"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

import django

from django.utils.encoding import force_str
from django.utils.encoding import smart_str
from django.utils.translation import gettext, gettext_lazy


django.utils.encoding.force_text = force_str
django.utils.encoding.smart_text = smart_str
django.utils.encoding.smart_unicode = smart_str
django.utils.translation.ugettext = gettext
django.utils.translation.ugettext_lazy = gettext_lazy
