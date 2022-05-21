long_text = 'Life is too short, you need python. ' * 10
print(long_text)

import textwrap
long_text = 'Life is too short, you need python. ' * 10
result = textwrap.wrap(long_text, width=70)
print("========================================================")
print(result)

print("========================================================")
print('\n'.join(result))


print("========================================================")
print(textwrap.fill(long_text, width=70))