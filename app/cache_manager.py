import time


class Cache:
    def __init__(self, expiry=60):
        self.cache = {}
        self.expiry = expiry  

    def set(self, key, value):
        self.cache[key] = (value, time.time() + self.expiry)

    def get(self, key):
        if key in self.cache:
            value, expiry_time = self.cache[key]
            if time.time() < expiry_time:
                return value
            else:
                del self.cache[key]
        return None

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def clear_expired(self):
        current_time = time.time()
        keys_to_delete = [key for key, (_, expiry_time) in self.cache.items() if current_time >= expiry_time]
        for key in keys_to_delete:
            del self.cache[key]
