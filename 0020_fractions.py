from fractions import Fraction

a = Fraction(1, 5)
b = Fraction(2, 5)

print(a + b)

result = a + b
print(result.denominator)
print(result)

c = Fraction(1, 2) + Fraction(1, 2)
print(c)

print(float(c))