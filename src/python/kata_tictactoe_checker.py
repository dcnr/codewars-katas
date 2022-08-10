"""
Tic-Tac-Toe Checker

If we were to set up a Tic-Tac-Toe game, we would want to know whether the
board's current state is solved, wouldn't we? Our goal is to create a function
that will check that for us!

Assume that the board comes in the form of a 3x3 array,
where the value is 0 if a spot is empty, 1
if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]

We want our function to return:

    -1 if the board is not yet finished AND no one has won yet
    (there are empty spots),
    1 if "X" won,
    2 if "O" won,
    0 if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a
game of Tic-Tac-Toe.

>>> is_solved([
... [0, 0, 1],
... [0, 1, 2],
... [2, 1, 0]])
-1

>>> is_solved([
... [1, 1, 1],
... [0, 2, 2],
... [0, 0, 0]])
1

>>> is_solved([
... [2, 1, 2],
... [2, 1, 1],
... [1, 2, 1]])
0

"""


def is_solved(board: list[list[int]]) -> int:
    """Checks if the current tic-tac-toe board is solved and returns who one.

    Args:
        board (list[list[int]]): The board to be checked.

    Returns:
        int: 1 if "X" won, 2 if "O" won, 0 if draw, -1 if it's not yet solved.
    """

    def compare(player: int) -> bool:
        if (
            set(board[0]) == {player}
            or set(board[1]) == {player}
            or set(board[2]) == {player}
            or set([board[0][0]] + [board[1][0]] + [board[2][0]]) == {player}
            or set([board[0][1]] + [board[1][1]] + [board[2][1]]) == {player}
            or set([board[0][2]] + [board[1][2]] + [board[2][2]]) == {player}
            or set([board[0][0]] + [board[1][1]] + [board[2][2]]) == {player}
            or set([board[0][2]] + [board[1][1]] + [board[2][0]]) == {player}
        ):
            return True

        return False

    if compare(1):
        return 1

    if compare(2):
        return 2

    if 0 in {tile for row in board for tile in row}:
        return -1

    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="is_solved", verbose=True)
