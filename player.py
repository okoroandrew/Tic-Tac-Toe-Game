import random

from move import Move


class Player:

    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human: bool):
        self._is_human = is_human

        if self.is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self.is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    @staticmethod
    def get_human_move():
        while True:
            value = int(input("Enter a move (1, 9): "))
            move = Move(value)
            if move.is_valid():
                return move
            else:
                print("your move is not valid, Enter a number between 0 and 9")

    @staticmethod
    def get_computer_move():
        value = random.randint(1, 9)
        move = Move(value)
        print(f"computer move is: {move.value}")
        return move




