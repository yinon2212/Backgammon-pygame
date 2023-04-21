import random, copy
from Cube import Cube


# This class represent a single turn in the game
class Turn:

    def __init__(self, ai_game):
        self.red_turn = True
        self.color = "red"
        self.player_clicks = []
        self.cubes = []
        self.chosen_cube = 0
        self.generate_cubes()
        self.source = None
        self.destination = None
        self.double_ind = -1
        self.ai_game = ai_game
        if ai_game:
            self.red_turn = False
            self.color = "white"
            self.ai_turn = True

    # This function changes the turns
    def change_turn(self):
        if self.ai_game:
            if self.ai_turn:
                self.ai_turn = False
                self.color = "red"
                self.red_turn = True
            else:
                self.ai_turn = True
                self.color = "white"
                self.red_turn = False
        else:
            if self.red_turn:
                self.red_turn = False
                self.color = "white"
            else:
                self.red_turn = True
                self.color = "red"
        self.generate_cubes()

    # This function generate 2 random number from 1-6 and insert them into the cubes array
    def generate_cubes(self):
        cube1 = Cube(random.randint(1, 6))
        cube2 = Cube(random.randint(1, 6))

        self.chosen_cube = 0

        if cube1.get_value() == cube2.get_value():
            self.cubes = [cube1, copy.deepcopy(cube1), copy.deepcopy(cube1), copy.deepcopy(cube1)]
            self.double_ind = 0
        else:
            self.cubes = [cube1, cube2]
            self.double_ind = -1

    # This function change the number of the chosen cube
    def set_chosen_cube(self, cube_number):
        self.chosen_cube = cube_number
        self.clear_clicks()

    # This function returns the number of steps
    def get_number_of_steps(self):
        return self.cubes[self.chosen_cube].get_value()

    # This function add new click to all the player clicks in this turn
    def add_click(self, click):
        self.player_clicks.append((click))

    # This function clears the player's clicks
    def clear_clicks(self):
        self.player_clicks.clear()

    # This function set new source to this turn
    def set_source(self, source):
        self.source = source

    # This function set the destination that the player need to transfer the chosen piece to
    def set_destination(self, destination, eat_piece, out_own_piece):
        self.destination = {"destination": destination, "eat_piece": eat_piece, "out_own_piece": out_own_piece}

    # This function removes the destination by setting his value to None
    def remove_destination(self):
        self.destination = None

    def remove_source(self):
        self.source = None

    # This function gets the cube number, and the played status
    # and set them to the cube that has the cube_number parameter value
    def set_cube_played(self, cube_number, played):
        self.cubes[cube_number].set_played(played)
        self.chosen_cube = 3 - (2 + cube_number)

    # This function returns True if all the cubes all benn played, and False if not
    def has_all_cubes_playes(self):
        for i in range(len(self.cubes)):
            if not self.cubes[i].get_played():
                break
        else:
            return True

        return False

    # This function increase the double index and by that continue to the next cube from the 4 cubes
    def increase_double_index(self):
        self.double_ind = self.double_ind + 1

    def __str__(self):
        return "Red turn: {0}, player clicks: {1}, cubes: {2}, chosen cube: {3}".format(self.red_turn,
                                                                                        self.player_clicks, self.cubes,
                                                                                        self.chosen_cube)
