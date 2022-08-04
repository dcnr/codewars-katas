"""
Codewars Kata - Sort the odd

Task

You will be given an array of numbers. You have to sort the odd numbers
in ascending order while leaving the even numbers at their original positions.

Examples

>>> sort_array([7, 1])
[1, 7]

>>> sort_array([5, 8, 6, 3, 4])
[3, 8, 6, 5, 4]

>>> sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""


def sort_array(source_array: list[int]) -> list[int]:
    """Sorts the odd number in ascending order while leaving the even numbers
    in place."""

    def is_odd(num: int) -> bool:
        """Checks if the number provided is odd."""
        return num % 2 == 1

    sorted_list: list[int] = source_array.copy()
    odd_list: list[int] = sorted(filter(is_odd, source_array))

    for idx, num in enumerate(source_array):
        if is_odd(num):
            sorted_list[idx] = odd_list.pop(0)

    return sorted_list


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="sort_array", verbose=True)
