# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals


class Client(object):
    cache = None
    db = None

    def __init__(self, hostname="127.0.0.1", port="11211", expiry=900):
        if hostname and port:
            from . import memcache_client

            self.cache = memcache_client.Client(hostname, port, expiry)

        from . import db_client

        self.db = db_client.Client()

    def set(self, key, value):
        """
        This method is used to set a new value
        in the memcache server and the db.
        """
        self.db.set(key, value)
        if self.cache:
            self.cache.set(key, value)

    def get(self, key):
        """Get a value from the memcache server or db."""
        if self.cache:
            value = self.cache.get(key) or self.db.get(key)
            if value:
                self.cache.set(key, value)
        else:
            v = self.db.get(key)
        return v
