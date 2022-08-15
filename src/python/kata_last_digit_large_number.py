"""
Last digit of a large number

Define a function that takes in two non-negative integers aaa and bbb and
returns the last decimal digit of aba^bab. Note that aaa and bbb may be
very large!

For example, the last decimal digit of 979^797 is 999, s
ince 97=47829699^7 = 478296997=4782969.
The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2200)2300,
which has over 109210^{92}1092 decimal digits, is 666.
Also, please take 000^000 to be 111.

You may assume that the input will always be valid.
Examples

>>> last_digit(4, 1)
4
>>> last_digit(4, 2)
6
>>> last_digit(9, 7)
9
>>> last_digit(10, 10 ** 10)
0
>>> last_digit(2 ** 200, 2 ** 300)
6

"""


def last_digit(num1: int, num2: int) -> int:
    """Returns the last digit of num1 raised to num2.

    Args:
        num1 (int): The base number.
        num2 (int): The exponent to raise base number.

    Returns:
        int: The last digit of the answer.
    """
    base = num1 % 10
    exp = num2 % 4
    return (base**exp if exp != 0 else base**4) % 10 if num2 != 0 else 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="last_digit", verbose=True)
