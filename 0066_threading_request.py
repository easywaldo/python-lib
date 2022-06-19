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
import threading

start = time.time()

pages = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
threads = []

for page in pages:
    t = threading.Thread(target=get_wikidocs, args=(page, ))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()
    
end = time.time()
print('수행시간 : %f 초' % (end - start))
