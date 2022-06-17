import http.client

def get_url(page):
    conn = http.client.HTTPSConnection('wikidocs.net')
    conn.request('GET', "/{}".format(page))
    
    r = conn.getresponse()
    with open('wikidocs_%s.html' % page, 'wb') as f:
        f.write(r.read())
    conn.close()
    

if __name__ == '__main__':
    get_url(12)