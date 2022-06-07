import urllib.request
from functools import lru_cache

@lru_cache(maxsize=32)
def get_url(page):
    print('get contents in url')
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'
    
first_6 = get_url(6)
first_7 = get_url(7)

second_6 = get_url(6)
second_7 = get_url(7)

assert first_6 == second_6
assert first_7 == second_7

