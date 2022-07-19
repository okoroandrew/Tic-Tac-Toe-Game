from move import Move
from player import Player


class Board:
    EMPTY_CELL = 0

    def __init__(self):
        self._board = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    def print_board(self):
        print("positions:\n")
        for row in self.board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()

    @staticmethod
    def print_board_positions():
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, move: Move, player: Player):
        row = move.get_row()
        column = move.get_column()

        if self.board[row][column] == Board.EMPTY_CELL:
            self.board[row][column] = player.marker
        else:
            print(f"position {move.value} already played. Please try again")

    def is_game_over(self, player: Player, last_move: Move):
        return (self.check_row(player, last_move)
                or self.check_column(player, last_move)
                or self.check_diagonal(player)
                or self.check_anti_diagonal(player))

    def check_row(self, player, last_move):
        row = last_move.get_row()
        if self.board[row].count(player.marker) == 3:
            return True

    def check_column(self, player: Player, last_move: Move) -> bool:
        column = last_move.get_column()
        board_column = []
        for row in self.board:
            board_column.append(row[column])
        if board_column.count(player.marker) == 3:
            return True

    def check_diagonal(self, player: Player):
        board_diagonal = [self.board[0][0], self.board[1][1], self.board[2][2]]
        if board_diagonal.count(player.marker) == 3:
            return True

    def check_anti_diagonal(self, player: Player):
        board_anti_diagonal = [self.board[0][2], self.board[1][1], self.board[2][0]]
        return board_anti_diagonal.count(player.marker) == 3

    def check_tie(self):
        num_of_empty_cells = 0
        for row in self.board:
            num_of_empty_cells += row.count(Board.EMPTY_CELL)

        return num_of_empty_cells == 0

    def reset_board(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]


