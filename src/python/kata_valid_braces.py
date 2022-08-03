"""
Codewars Kata - Valid Braces

Write a function that takes a string of braces, and determines if the
order of the braces is valid. It should return true if the string is valid,
and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new
characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses,
brackets and curly braces: ()[]{}.
What is considered Valid?

A string of braces is considered valid if all braces are matched with
the correct brace.

Examples:

>>> valid_braces("(){}[]")
True
>>> valid_braces("([{}])")
True
>>> valid_braces("(}")
False
>>> valid_braces("[(])")
False
>>> valid_braces("[({})](]")
False

"""


def valid_braces(sequence: str) -> bool:
    """Returns the validity of a given sequence of brackets.

    >>> valid_braces("()")
    True
    >>> valid_braces("(}")
    False
    """

    open_: str = "[({"
    close_: str = "])}"
    buff: list[str] = []

    for brace in sequence:
        # Append opening brace
        if brace in open_:
            buff.append(brace)

        else:
            # Closing brace first in line
            if len(buff) == 0:
                return False

            # Popped last input should be equal to closing brace
            if buff.pop() != open_[close_.find(brace)]:
                return False

    # Remaining braces are unclosed
    if len(buff) != 0:
        return False

    return True


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="valid_braces", verbose=True)
