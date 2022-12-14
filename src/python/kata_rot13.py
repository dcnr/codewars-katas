"""
ROT13

How can you tell an extrovert from an introvert at NSA? Va gur ryringbef,
gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can
decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13)
is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces,
punctuation, numbers etc.

Test examples:

>>> rot13("EBG13 rknzcyr.")
'ROT13 example.'

>>> rot13("This is my first ROT13 excercise!")
'Guvf vf zl svefg EBG13 rkprepvfr!'
"""

import codecs


def rot13(message: str) -> str:
    """Applies ROT13 to message.

    Args:
        message (str): The input string to be encoded.

    Returns:
        str: The ROT13 message.
    """
    return codecs.encode(message, "rot13")


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="rot13", verbose=True)
