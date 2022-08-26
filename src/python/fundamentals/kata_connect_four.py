"""
Connect 4

Introduction

We all love to play games especially as children. I have fond memories playing
Connect 4 with my brother so decided to create this Kata based on the classic
game. Connect 4 is known as several names such as “Four in a Row” and
“Captain’s Mistress" but was made popular by Hasbro MB Games

Task

The game consists of a grid (7 columns and 6 rows) and two players that take
turns to drop their discs. The pieces fall straight down, occupying the next
available space within the column. The objective of the game is to be the first
to form a horizontal, vertical, or diagonal line of four of one's own discs.

Your task is to create a Class called Connect4 that has a method called play
which takes one argument for the column where the player is going to place
their disc.

Rules

If a player successfully has 4 discs horizontally, vertically or diagonally
then you should return "Player n wins!” where n is the current player either 1
or 2.

If a player attempts to place a disc in a column that is full then you should
return ”Column full!” and the next move must be taken by the same player.

If the game has been won by a player, any following moves should return ”Game
has finished!”.

Any other move should return ”Player n has a turn” where n is the current player
either 1 or 2.

Player 1 starts the game every time and alternates with player 2.

The columns are numbered 0-6 left to right.

Good luck and enjoy!
"""

from dataclasses import dataclass


@dataclass
class Piece:
    """Represents the player piece"""

    owner: int
    col: int
    row: int

    def __repr__(self) -> str:
        return f"P{self.owner}: {self.col},{self.row}"


@dataclass
class Direction:
    """Represents a direction from the current piece."""

    name: str
    row_offset: int
    col_offset: int


class Connect4:
    """Connect 4 the game!"""

    def __init__(self):
        self.grid: list[list[Piece]] = [
            [0 for _ in range(7)] for _ in range(6)
        ]

        self.current_player: int = 1
        self.game_won: bool = False

        self.directions = [
            Direction("North West", -1, -1),
            Direction("North", 0, -1),
            Direction("North East", 1, -1),
            Direction("West", -1, 0),
            Direction("East", 1, 0),
            Direction("South West", -1, 1),
            Direction("South", 0, 1),
            Direction("South East", 1, 1),
        ]

    def play(self, col: int) -> str:
        """Adds the player's piece to the playing field.

        Args:
            col (int): The column where to add the piece.

        Returns:
            str: Current game status.
        """
        if self.game_won:
            return "Game has finished!"

        for row, grid_row in reversed(list(enumerate(self.grid))):
            if grid_row[col] == 0:
                player_piece = Piece(self.current_player, col, row)
                grid_row[col] = player_piece
                player = self.current_player

                if self.check_win(player_piece):
                    self.game_won = True
                    return f"Player {player} wins!"

                self.current_player = 2 if self.current_player == 1 else 1
                return f"Player {player} has a turn"

        return f"Column full!"

    def show_field(self):
        """Shows game field."""
        for row in self.grid:
            print("\t", row)

    def check_win(self, curr_piece: Piece) -> bool:
        """Checks if the player has won.

        Args:
            curr_piece (Piece): The current piece.

        Returns:
            bool: True if won, else False.
        """
        for direction in self.directions:
            if self.direction_check(
                direction.col_offset, direction.row_offset, curr_piece
            ):
                return True

        return False

    def direction_check(
        self, col_offset: int, row_offset: int, curr_piece: Piece, ctr: int = 0
    ) -> bool:
        """Checks if there's a winning line of pieces in direction.

        Args:
            col_offset (int): The next column to check.
            row_offset (int): The next row to check.
            curr_piece (Piece): The current piece for reference.
            ctr (int): Count of winning pieces. Defaults to 0

        Returns:
            bool: True if winning, else False.
        """
        if ctr == 3:
            return True

        next_piece = self.get_next_piece(
            curr_piece.col + col_offset, curr_piece.row + row_offset
        )

        if isinstance(next_piece, Piece):
            if next_piece.owner == curr_piece.owner:
                return self.direction_check(
                    col_offset, row_offset, next_piece, ctr + 1
                )

        return False

    def get_next_piece(self, col: int, row: int) -> Piece | bool:
        """Tries to get the next piece.

        Args:
            col (int): Column of next piece.
            row (int): Row of next piece.

        Returns:
            Piece | bool: Returns the next piece if able, False if not.
        """
        try:
            next_piece = self.grid[row][col]
        except IndexError:
            return False

        return next_piece


if __name__ == "__main__":
    game = Connect4()
    print(game.play(2))
    print(game.play(1))
    print(game.play(0))
    print(game.play(2))
    print(game.play(1))
    print(game.play(0))
    print(game.play(0))
    print(game.play(1))
    print(game.play(2))
    print(game.play(0))
    print(game.play(1))
    print(game.play(3))
    print(game.play(5))
