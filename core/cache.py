_cache = {}

def get_cache(key):
    return _cache.get(key)

def set_cache(key, value):
    _cache[key] = value
