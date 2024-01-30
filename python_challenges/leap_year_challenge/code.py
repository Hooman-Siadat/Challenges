def is_leap(year):
		"""
    Check if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked for leap year status.

    Returns:
    - bool: True if the year is a leap year, False otherwise.

    Leap year conditions:
    1. The year must be divisible by 4.
    2. If the year is divisible by 100, it must also be divisible by 400.

    Examples:
    >>> is_leap(1992)
    True
    >>> is_leap(1900)
    False
    >>> is_leap(2000)
    True
    """
    leap = False
    
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap

year = 1992

print(is_leap(year))
