from enum import Enum
import random as r
import termcolor as tc

class terrain_types(Enum):
     entry_point = "+"
     exit_point = tc.colored("X", "light_blue")
     empty = " "
     asteroids = "%"
     orbit = "O"
     trade_post = tc.colored("T", "light_green")

terrain_weights = [0, 0, 20, 3, 1, 1]

class Terrain():
        def __init__(self):
            self.type = r.choice(r.choices(list(terrain_types), terrain_weights, k=100))
            self.name = self.type.name
            self.icon = self.type.value

        def set_type(self, type : terrain_types):
            self.type = type
            self.name = self.type.name
            self.icon = self.type.value

class Tile():
    def __init__(self, terrain : Terrain, contents : list):
        self.terrain = terrain
        self.contents = contents

class Map():
    def __init__(self, x, y):
        self.x_dim = x
        self.y_dim = y
        self.data = [[Tile(Terrain(), r.randint(0, 10)) for j in range(self.x_dim)] for i in range(self.y_dim)]
        self.discovered = [[False for j in range(self.x_dim)] for i in range(self.y_dim)]
        self.start_location = [r.randint(0, self.x_dim - 1), r.randint(0, self.y_dim - 1)]
        self.exit_location = [r.randint(0, self.x_dim - 1), r.randint(0, self.y_dim - 1)]
        
        while self.start_location == self.exit_location:
            self.exit_location = [r.randint(0, self.x_dim - 1), r.randint(0, self.y_dim - 1)]

        self.data[self.start_location[1]][self.start_location[0]].terrain.set_type(terrain_types.entry_point)
        self.data[self.exit_location[1]][self.exit_location[0]].terrain.set_type(terrain_types.exit_point)

    def render(self, player_pos):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if player_pos[0] == x and player_pos[1] == y:
                    print("["+ tc.colored("@", "light_blue") +"]", end="")
                elif not self.discovered[y][x]:
                    print(tc.colored("[?]", "red"), end="")
                else:
                    print(f"[{self.data[y][x].terrain.icon}]", end="")
            print("")