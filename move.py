class Move:

    def __init__(self, value):
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def is_valid(self) -> bool:
        if self._value in range(1, 10):
            return True
        else:
            return False

    def get_row(self):
        if self.value in (1, 2, 3):           # 1 2 3
            return 0
        elif self.value in (4, 5, 6):         # 4 5 6
            return 1
        elif self.value in (7, 8, 9):                                   # 7 8 9
            return 2

    def get_column(self):
        if self.value in (1, 4, 7):
            return 0
        elif self.value in (2, 5, 8):
            return 1
        elif self.value in (3, 6, 9):
            return 2


