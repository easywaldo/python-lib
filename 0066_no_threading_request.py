import urllib.request

def get_wikidocs(page):
    print('wikidocs page:{}'.format(page))
    resource = 'https://wikidocs.net/{}'.format(page)
    
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError as e:
        return 'Not Found'


import time

start = time.time()
pages = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

for page in pages:
    get_wikidocs(page)
    
end = time.time()

print('수행시간 : %f 초' % (end - start))