# Leap Year Challenge

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

1. The year can be evenly divided by 4; it is a leap year unless:
2. The year can be evenly divided by 100; it is NOT a leap year, unless:
3. The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are NOT leap years. (Source)

## Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean `True`; otherwise, return `False`.

Note that the code stub provided reads from STDIN and passes arguments to the `is_leap` function. It is only necessary to complete the `is_leap` function.

---

## Python Solution

```Python
def is_leap(year):
    """
    Determine if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    - bool: True if the year is a leap year, False otherwise.

    Example:
    >>> is_leap(2000)
    True

    >>> is_leap(1900)
    False
    """
    leap = False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap


year = int(input('Enter a year in YYYY format:'))

print(f'{year} is a leap year!') if is_leap(year) else print(f'{year} is not a leap year!')

```
