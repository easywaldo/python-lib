import pickle

data = {}
data[1] = {'no': 1, 'subject': 'hello pickle', 'content': 'pickle is very simple'}

with open('data.p', 'wb') as f:
    pickle.dump(data, f)

with open('data.p', 'rb') as f:
    data = pickle.load(f)

print(data)
