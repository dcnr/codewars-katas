"""
Codewars Kata - Your order, please

Your task is to sort a given string. Each word in the string will
contain a single number. This number is the position the word should
have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

Examples:

>>> order("is2 Thi1s T4est 3a")
'Thi1s is2 3a T4est'

>>> order("4of Fo1r pe6ople g3ood th5e the2")
'Fo1r the2 g3ood 4of th5e pe6ople'

>>> order("")
''

"""


def order(sentence: str) -> str:
    """Sorts a given string according to the consecutive numbers embedded
    in the words."""

    words: list[str] = sentence.split()
    word_list: list[str] = [""] * len(words)

    for word in words:
        for char in word:
            if char.isdigit():
                word_list[int(char) - 1] = word
                break

    return " ".join(word_list)


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="order", verbose=True)
