"""
Codewars Kata - Two Sum

Write a function that takes an array of numbers (integers for the tests)
and a target number. It should find two different items in the array that,
when added together, give the target value. The indices of these items
should then be returned in a tuple / list (depending on your language)
like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers;
any valid solutions will be accepted.

The input will always be valid (numbers will be an array of
length 2 or greater, and all of the items will be numbers;
target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

>>> two_sum([1, 2, 3], 4)
[0, 2]

>>> two_sum([1234,5678,9012], 14690)
[1, 2]

>>> two_sum([0, 0], 0)
[0, 1]
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    """Returns the indices of the numbers that add up to target number.

    Args:
        numbers (list[int]): The number list
        target (int): The target number

    Returns:
        list[int]: The list of indices of the numbers that add up to target
    """

    index_pair: list[int] = []

    for idx, first_addend in enumerate(numbers):
        second_addend = target - first_addend
        if second_addend in numbers:
            index_pair = [idx, numbers.index(second_addend, idx + 1)]
            break

    return index_pair


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="two_sum", verbose=True)
