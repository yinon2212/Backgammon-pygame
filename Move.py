
# This function represent each move, when the player click it set the row_from and col_from params,
# and when he click again, it set the row_to, and col_to params
class Move:

    def __init__(self, row_from, col_from):
        self.row_from = row_from
        self.col_from = col_from
        self.row_to = -1
        self.col_to = -1
        self.have_dest = False

    # This function returns the value of the row_from parameter
    def get_row_from(self):
        return self.row_from

    # This function returns the value of the col_from parameter
    def get_col_from(self):
        return self.col_from

    def set_row_from(self, row):
        self.row_from = row

    def set_col_from(self, col):
        self.col_from = col

    # This function returns the value of the row_to parameter
    def get_row_to(self):
        return self.row_to

    # This function returns the value of the col_to parameter
    def get_col_to(self):
        return self.col_to

    # This function set the row to and the col to parameters
    def set_row_col_to(self, row_to, col_to):
        self.row_to = row_to
        self.col_to = col_to
        self.have_dest = True

    def __eq__(self, move):
        return self.row_from == move.row_from and self.col_from == move.col_from

    def __hash__(self):
        return hash((self.row_from, self.col_from))

    def __str__(self):

        return "From({0}, {1}) ==> To({2}, {3})".format(self.row_from, self.col_from, self.row_to, self.col_to)
