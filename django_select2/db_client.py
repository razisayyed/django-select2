# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .models import KeyMap


class Client(object):
    def set(self, key, value):
        """
        This method is used to set a new value
        in the db.
        """
        KeyMap.objects.update_or_create(key=key, value=value)

    def get(self, key):
        """
        This method is used to retrieve a value
        from the db.
        """
        return KeyMap.objects.filter(key=key).first()
