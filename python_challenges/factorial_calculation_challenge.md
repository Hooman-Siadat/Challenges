# Factorial Calculation Challenge

Write a recursive function to calculate the factorial of a non-negative integer n, denoted as n!. The factorial of n is the product of all positive integers less than or equal to n.
---

## Python Solution
```python
def fact(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(-10))
```