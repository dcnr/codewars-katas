"""
Find the Unique Number

There is an array with some numbers. All numbers are equal except for one.
Try to find it!

>>> find_uniq([ 1, 1, 1, 2, 1, 1 ])
2
>>> find_uniq([ 0, 0, 0.55, 0, 0 ])
0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

from collections import Counter


def find_uniq(arr: list[float]) -> float:
    """Returns the unique number in the list.

    Args:
        arr (list[float]): The source list.

    Returns:
        float: The unique number.
    """
    return Counter(arr).most_common()[:-2:-1][0][0]


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="find_uniq", verbose=True)
