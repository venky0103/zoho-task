import unittest
from menu.menu_cache import MenuCache
from time import sleep

class TestCache(unittest.TestCase):
    def test_cache_addition_eviction(self):
        cache = MenuCache(max_size=2, eviction_time=2)
        cache.add("item1", "value1")
        cache.add("item2", "value2")
        self.assertEqual(len(cache.cache), 2)
        cache.add("item3", "value3")
        self.assertEqual(len(cache.cache), 2)
        self.assertNotIn("item1", cache.cache)

    def test_cache_time_based_eviction(self):
        cache = MenuCache(max_size=3, eviction_time=1)
        cache.add("item1", "value1")
        sleep(2)
        cache.add("item2", "value2")
        cache._evict_old_entries()
        self.assertNotIn("item1", cache.cache)

if __name__ == '__main__':
    unittest.main()
