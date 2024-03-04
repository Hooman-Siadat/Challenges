
# Leap Year Challenge

Implement a recursive function to generate the nth term of the Fibonacci sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.

## Task

1- Test Case 1: Fibonacci of 0

Input: 0
Expected Output: 0

2- Test Case 2: Fibonacci of 1

Input: 1
Expected Output: 1

3- Test Case 3: Fibonacci of 5

Input: 5
Expected Output: 5

4- Test Case 4: Fibonacci of 10

Input: 10
Expected Output: 55

5- Test Case 8: Fibonacci of 30

Input: 30
Expected Output: 832040

---

## Python Solution

```Python
def fib(n):
    if n < 0:
        raise ValueError("Fibonacci sequence startes from 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)


print(fib(30))
```
