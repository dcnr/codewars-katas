"""
Codewars Kata - Extract the domain name from URL

Write a function that when given a URL as a string,
parses out just the domain name and returns it as a string.

Example:

>>> domain_name("http://github.com/carbonfive/raygun")
'github'

>>> domain_name("http://www.zombie-bites.com")
'zombie-bites'

>>> domain_name("https://www.cnet.com")
'cnet'

"""

from typing import Any

import re


def domain_name(url: str) -> Any:
    """Returns the domain name from a given URL

    Args:
        url (str): The given URL

    Returns:
        Any: The domain name
    """
    res: Any = re.search(r"(www.)*([a-zA-Z0-9\-]+)\.([a-zA-Z]+)", url)
    return res.group(2)


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="domain_name", verbose=True)
