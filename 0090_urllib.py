import urllib.request

def get_wikidocs(page):
    print('wikidocs page: {}'.format(page))
    resource = 'https://wikidocs.net/{}'.format(page)
    
    with urllib.request.urlopen(resource) as s:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(s.read())
            
if __name__ == '__main__':
    get_wikidocs(11)
