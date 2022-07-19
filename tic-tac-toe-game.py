import os

from board import Board
from player import Player


class Game:

    def start_game(self):
        print("----------------------------------")
        print("      Welcome To Tic-Tac-Toe      ")
        print("----------------------------------")

        board = Board()
        human_player = Player(is_human=True)
        computer_player = Player(is_human=False)

        while True:
            while True:
                player_move = human_player.get_move()
                board.submit_move(player_move, human_player)
                board.print_board()

                if board.is_game_over(human_player, player_move):
                    print("You won!!!")
                    break
                elif board.check_tie():
                    print("Its a tie")
                    break

                else:
                    computer_move = computer_player.get_move()
                    board.submit_move(computer_move, computer_player)
                    board.print_board()

                    if board.is_game_over(computer_player, computer_move):
                        print("Computer won")
                        break

            play_again = input("Play again?: press Y to play again or N to stop: ").lower()

            if play_again == "n":
                print("Game over.")
                break
            else:
                self.start_new_game(board)

    def start_new_game(self, board: Board):
        os.system("clear")
        print("---------------------------------------")
        print("               New Round               ")
        print("---------------------------------------")
        board.reset_board()
        board.print_board()


game = Game()
game.start_game()
