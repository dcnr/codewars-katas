"""
Exes and ohs

Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

>>> xo("ooxx")
True
>>> xo("xooxx")
False
>>> xo("ooxXm")
True

Should return True if there are no x's or o's

>>> xo("zpzpzpp")
True
>>> xo("zzoo")
False
"""


def xo(s) -> bool:
    """Checks if input string has same amount of 'x's and 'o's.

    Args:
        s (str): Input string.

    Returns:
        bool: True if there are same amount of x's and o's. False if not.
    """
    return s.lower().count("x") == s.lower().count("o")


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="xo", verbose=True)
