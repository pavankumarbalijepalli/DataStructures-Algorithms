# Recursion

## Power of a num
from random import randint as rnd


def power(base, exp):
	if exp <= 1:
		return base
	return base * power(base, exp - 1)

print(power(-2.2, 2))

## Find GCD of Two Numbers

def GCD(x, y):
    assert int(x)==x and int(y)==y, "Please send only integers"
    x, y = abs(x), abs(y)
    if y == 0:
        return x
    return GCD(y, x%y)
    
print(GCD(48, 18))

## Conver Decimal to Binary

def dec2bin(n: int):
    if n == 0:
        return 1
    return 10*dec2bin(n//2) + n%2

q = rnd(0, 100)
print(q, dec2bin(q))