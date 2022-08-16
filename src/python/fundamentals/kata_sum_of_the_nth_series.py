"""
Sum of the first nth term of Series

Task:

Your task is to write a function which returns the sum of following series upto
nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:

    You need to round the answer to 2 decimal places and return it as String.

    If the given value is 0 then it should return 0.00

    You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)

1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
>>> series_sum(1)
'1.00'
>>> series_sum(2)
'1.25'
>>> series_sum(5)
'1.57'
"""


def series_sum(iterations: int) -> str:
    """Returns the sum of the first nth number in the series.

    Args:
        iterations (int): The number of iterations to do.

    Returns:
        float: The sum of the number series.
    """
    if not iterations:
        return "0.00"

    sum_: float = 1.00
    divisor: int = 4
    for _ in range(iterations - 1):
        sum_ += 1 / divisor
        divisor += 3

    return f"{sum_:0.2f}"


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="series_sum", verbose=True)
