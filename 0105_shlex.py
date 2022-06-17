import shlex

result = shlex.split('This is a "test"')
print(result)

result = shlex.split('This is "a test"', posix=False)
print(result)