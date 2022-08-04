"""
Codewars Kata - Bit Counting

Write a function that takes an integer as input, and returns the number of
bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010,
so the function should return 5 in this case

Example:

>>> count_bits(1234)
5

>>> count_bits(4)
1
"""


def count_bits(num: int) -> int:
    """Returns the number of bits that are equal to one in the binary
    representation of the number.

    Args:
        num (int): The number to be converted to binary

    Returns:
        int: The number of bits equal to 1
    """
    return bin(num).count("1")


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="count_bits", verbose=True)
