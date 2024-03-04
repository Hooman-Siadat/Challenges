
# Leap Year Challenge

Write a recursive function to calculate the exponentiation of a base `b` raised to a non-negative integer exponent `e`. For example, `power(2, 3)` should return `8` (2 raised to the power of 3).

## Task

1- Test Case 1: Base raised to the power of 0

`Input: Base = 5, Exponent = 0
Expected Output: 1` (Any number raised to the power of 0 equals 1)

2- Test Case 2: Base raised to the power of 1

`Input: Base = 3, Exponent = 1
Expected Output: 3` (Any number raised to the power of 1 equals the number itself)

3- Test Case 3: Base raised to a positive integer exponent

`Input: Base = 2, Exponent = 5
Expected Output: 32` (2 raised to the power of 5 equals 32)

4- Test Case 4: Base raised to the power of 10

`Input: Base = 10, Exponent = 10
Expected Output: 10000000000` (10 raised to the power of 10 equals 10,000,000,000)

5- Test Case 5: Base raised to the power of 7

`Input: Base = 3, Exponent = 7
Expected Output: 2187` (3 raised to the power of 7 equals 2187)

---

## Python Solution

```Python
def power(base, exponent, /):
    # base case
    if base == 0:
        return 0

    if exponent < 0:
        raise ValueError('Exponent value can not be negative!')
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base

    return base * power(base, exponent-1)


print(power(4, -3))
```
