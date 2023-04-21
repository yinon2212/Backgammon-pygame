from Piece import Piece


# This class represent a player
class Player:

    def __init__(self, type, positions):
        self.type = type
        self.pieces = []
        self.set_pieces(positions)
        self.eaten = []
        self.row_home = 0
        if type == "white":
            self.row_home = 1
        self.all_home = False

    # This function returns all the pieces of the current player
    def get_pieces(self):
        return self.pieces

    # This function set all the pieces of the current player
    def set_pieces(self, positions):
        image = "white.png"
        if self.type == "red":
            image = "red.png"

        for i in range(15):
            x = int(positions[i][1]/263)
            y = int(positions[i][0]/75)
            self.pieces.append(Piece(self.type, image, x, y, positions[i][0], positions[i][1]))

    def add_piece(self, piece):
        self.pieces.append(piece)

    # This function organize the pieces as they should be on the beginning of he game
    def start_game(self):
        if self.type == "red":
            pass
        elif self.type == "white":
            pass

    # This function removes from the available pieces the piece that has been eaten and add it to the eaten pieces array
    def add_piece_eaten(self, piece):
        self.eaten.append(piece)

    # This function set the all_home parameter
    def set_all_home(self, all__home):
        self.all_home = all__home

    # This function returns all the data about each piece of the pieces that the player has
    def __str__(self):
        pieces = []
        for piece in self.pieces:
            pieces.append(piece.__str__())
            pieces.append("-------------------\n")

        return " ".join(pieces)