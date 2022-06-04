import math

print(math.gcd(60, 100))

# python 3.9 이상
# print(math.lcm(15, 25))

print(0.1 * 3 == 0.3)
print(math.isclose(0.1 * 3, 0.3))

print(1.2 - 0.1 == 1.1)
print(math.isclose(1.2 - 0.1, 1.1))

from decimal import Decimal
print(Decimal('0.1') * 3)
print(Decimal('1.2') - Decimal('0.1'))
print(Decimal('0.1') * Decimal('0.1'))

print(float(Decimal('1.2') - Decimal('0.1')) == 1.1)
