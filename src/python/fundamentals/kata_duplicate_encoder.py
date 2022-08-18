"""
Duplicate encoder

The goal of this exercise is to convert a string to a new string where each
character in the new string is "(" if that character appears only once in the
original string, or ")" if that character appears more than once in the original
string. Ignore capitalization when determining if a character is a duplicate.
Examples

>>> duplicate_encode("din")
'((('
>>> duplicate_encode("recede")
'()()()'
>>> duplicate_encode("Success")
')())())'
>>> duplicate_encode("(( @")
'))(('

Notes

Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result,
not the input!

"""


def duplicate_encode(word: str) -> str:
    """Encodes the characters in the input. "(" if the character only exists
    once, ")" otherwise.

    Args:
        word (str): The souce string.

    Returns:
        str: The encoded string.
    """
    word = word.lower()
    return "".join("(" if word.count(char) == 1 else ")" for char in word)


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="duplicate_encode", verbose=True)
