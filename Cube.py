
# This class represent a single cube
class Cube():

    def __init__(self, value):
        self.value = value  # The value of the cube (1-6)
        self.played = False  # True if the cube has been played and False if not

    # This function returns the current value of the cube
    def get_value(self):
        return self.value

    # This function set new value to the cube
    def set_value(self, value):
        self.value = value

    # This function returns the current value of the parameter played
    def get_played(self):
        return self.played

    # THis function set the played parameter
    # If the player decided to play with the cube, it will become True
    # If the program generates new cube it will become False
    def set_played(self, played):
        self.played = played

    def __str__(self):
        return "Value: {0}".format(self.value)



