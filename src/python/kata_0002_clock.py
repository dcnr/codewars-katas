"""
Codewars - Beginner Series #2 Clock

Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since
midnight in milliseconds.


Example:

h = 0
m = 1
s = 1

result = 61000

Input constraints:

    0 <= h <= 23
    0 <= m <= 59
    0 <= s <= 59
"""


def past(hour: int, minute: int, second: int) -> int:
    """Returns elapsed time from midnight in milliseconds."""
    return (hour * 3600000) + (minute * 60000) + (second * 1000)
