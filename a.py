from Board import Board
from Turn import Turn
from Player import Player
from Ai_player import Ai
from Move import Move

# Piece positions for the start of the game for WHITE and RED
WHITE_PLACES = [(25, 20), (25, 76), (25, 132), (25, 188),
                (25, 56), (315, 486), (315, 430), (315, 374), (515, 486), (515, 430), (515, 374), (515, 318),
                (515, 450), (878, 20), (878, 76)]

RED_PLACES = [(25, 486), (25, 430), (25, 374), (25, 318), (25, 450), (310, 20), (310, 76), (310, 132),
              (518, 20), (518, 76), (518, 132), (518, 188), (518, 56), (875, 486), (875, 430)]

red_player = Player("red", RED_PLACES)
white_player = Player("white", WHITE_PLACES)
board = Board(red_player, white_player)
turn = Turn(True)

ai_player = Ai("white", WHITE_PLACES, board, turn)

print("Done")

