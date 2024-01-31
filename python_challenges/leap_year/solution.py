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

print(is_leap(year))
