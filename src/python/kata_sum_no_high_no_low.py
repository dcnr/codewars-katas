"""
Codewars Kata - Sum without highest and lowest number

Task

Sum all the numbers of a given array ( cq. list ), except the highest and the
lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge,
even if there are more than one with the same value.

Mind the input validation.
Example

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6

Input validation

If an empty value ( null, None, Nothing etc. ) is given instead of an array,
or the given array is an empty list or a list with only 1 element, return 0.
"""


def sum_array(num_list: list[int]) -> int:
    """Returns the sum of all elements excluding the highest and lowest."""

    if not hasattr(num_list, "__iter__") or len(num_list) <= 1:
        return 0

    return sum(num_list) - min(num_list) - max(num_list)


if __name__ == "__main__":
    # print(sum_array(None), 0)  # mypy error but needed for testing purposes
    print(sum_array([]), 0)
    print(sum_array([3]), 0)
    print(sum_array([1, 2]), 0)
    print(sum_array([6, 2, 1, 8, 10]), 16)
