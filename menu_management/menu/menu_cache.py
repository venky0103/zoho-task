import gzip
from collections import OrderedDict
from time import time

class MenuCache:
    def __init__(self, max_size, eviction_time=21600):  # 6 hours = 21600 seconds
        self.cache = OrderedDict()
        self.max_size = max_size
        self.eviction_time = eviction_time

    def _evict_old_entries(self):
        current_time = time()
        keys_to_evict = [key for key, (_, timestamp) in self.cache.items() if current_time - timestamp > self.eviction_time]
        for key in keys_to_evict:
            del self.cache[key]

    def _compress(self, value):
        return gzip.compress(value.encode('utf-8'))

    def _decompress(self, compressed_value):
        return gzip.decompress(compressed_value).decode('utf-8')

    def add(self, key, value):
        self._evict_old_entries()
        compressed_value = self._compress(value)
        if key in self.cache:
            del self.cache[key]  # remove old entry to update its position
        elif len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)  # remove the oldest item
        self.cache[key] = (compressed_value, time())

    def get(self, key):
        self._evict_old_entries()
        if key in self.cache:
            compressed_value, _ = self.cache.pop(key)
            self.cache[key] = (compressed_value, time())  # update the timestamp
            return self._decompress(compressed_value)
        return None

    def __repr__(self):
        return f"MenuCache(size={len(self.cache)}, max_size={self.max_size})"
