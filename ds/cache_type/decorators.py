from functools import wraps
from ds import LFUCache, Cache, LRUCache

__all__ = [
    "cache",
    "lfu_cache",
    "lru_cache",
]


def cache(capacity: int = 1024):
    """A decorator to cache function results using a standard cache."""
    cache = Cache(capacity=capacity)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create a cache key from arguments
            cache_key = (args, frozenset(kwargs.items()))
            result = cache.get(cache_key)

            if result is not None:
                return result

            # Compute result if not in cache
            result = func(*args, **kwargs)
            cache.put(cache_key, result)
            return result

        return wrapper

    return decorator


def lfu_cache(capacity: int = 1024):
    """A decorator to cache function results using the LFU (Least Frequently Used) policy."""
    cache = LFUCache(capacity=capacity)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create a cache key from arguments
            cache_key = (args, frozenset(kwargs.items()))
            result = cache.get(cache_key)

            if result is not None:
                return result

            # Compute result if not in cache
            result = func(*args, **kwargs)
            cache.put(cache_key, result)
            return result

        return wrapper

    return decorator


def lru_cache(capacity: int = 1024):
    """A decorator to cache function results using the LRU (Least Recently Used) policy."""
    cache = LRUCache(capacity=capacity)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create a cache key from arguments
            cache_key = (args, frozenset(kwargs.items()))
            result = cache.get(cache_key)

            if result is not None:
                return result

            # Compute result if not in cache
            result = func(*args, **kwargs)
            cache.put(cache_key, result)
            return result

        return wrapper

    return decorator
