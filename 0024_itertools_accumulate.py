import imp


import itertools

monthly_income = [1200, 1100, 900, 1450, 1600, 1100, 800, 1800, 1400, 1500, 1920]
result = list(itertools.accumulate(monthly_income))
print(result)

result = list(itertools.accumulate(monthly_income, max))
print(result)