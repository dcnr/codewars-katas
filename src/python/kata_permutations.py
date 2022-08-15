"""
Permutations

In this kata you have to create all permutations of a non empty input string
and remove duplicates, if present. This means, you have to shuffle all letters
from the input in all possible orders.

Examples:

>>> permutations('a')
['a']
>>> permutations('ab')
['ab', 'ba']
>>> permutations('aabb')
['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

The order of the permutations doesn't matter.

"""

import itertools


def permutations(string: str) -> list[str]:
    """Returns the permutations of input string.

    Args:
        string (str): Input string.

    Returns:
        list[str]: List of permutations.
    """
    return sorted(
        list({"".join(group) for group in itertools.permutations(string)})
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="permutations", verbose=True)
