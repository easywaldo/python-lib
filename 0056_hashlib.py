import hashlib

m = hashlib.sha256()

m.update('Life is too short'.encode('utf-8'))
m.update(', you need python.'.encode('utf-8'))


print(m.digest())
print(m.hexdigest())


import os

def check_password():
    if os.path.exists('password.txt'):
        before_password = input('input your old password : ')
        m = hashlib.sha256()
        m.update(before_password.encode('utf-8'))
        with open('password.txt', 'r') as f:
            return m.hexdigest() == f.read()
    else:
        return True

if check_password():
    password = input('Enter your new password : ')
    with open('password.txt', 'w') as f:
        m = hashlib.sha256()
        m.update(password.encode('utf-8'))
        f.write(m.hexdigest())
else:
    print('password is not match')
