import gzip

data = "Life is too short, You need python." * 1000

with gzip.open('data.txt.gz', 'wb') as f:
    f.write(data.encode('utf-8'))
    
with gzip.open('data.txt.gz', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data