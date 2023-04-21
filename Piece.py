# This class represent a single piece on the board (red or white)
class Piece:
    def __init__(self, color, image, row, col, row_visual, col_visual):
        self.color = color
        self.image = image
        self.row = row
        self.col = col
        self.row_visual = row_visual
        self.col_visual = col_visual

    # This function returns the color of the Piece
    def get_color(self):
        return self.color

    # This function returns the image of the Piece
    def get_img(self):
        return self.image

    # This function returns the current row of the Piece
    def get_row(self):
        return self.row

    # This function set the current row to the given row
    def set_row(self, row):
        self.row = row

    # This function returns the current column of the Piece
    def get_col(self):
        return self.col

    # This function change the current column to the given column
    def set_col(self, col):
        self.col = col

    # This function returns the current row visual of the Piece
    def get_row_visual(self):
        return self.row_visual

    # This function change the current row visual to the given row visual
    def set_row_visual(self, row_visual):
        self.row_visual = row_visual

    # This function returns the current column visual of the Piece
    def get_col_visual(self):
        return self.col_visual

    # This function change the current column visual to the given column
    def set_col_visual(self, col_visual):
        self.col_visual = col_visual

    # This function returns True if the two pieces have the same row and col, and if not it returns False
    def __eq__(self, piece):
        return self.row == piece.row and self.col == piece.col

    def __hash__(self):
        return hash((self.row, self.col))

    # This function returns all the data about the piece
    def __str__(self):
        return "Color = {0}\nImage = {1}\nRow = {2}\nColumn = {3}\n".format(self.color, self.image, self.row, self.col)
