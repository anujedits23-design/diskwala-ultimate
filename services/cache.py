CACHE = {}

def get(link):
    return CACHE.get(link)

def set(link, value):
    CACHE[link] = value
