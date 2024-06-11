from enum import Enum


class World:
    # formatting for the user
    class Tiles(Enum):
        empty = [".", 0]
        wall = ["#", 1]
        player = ["P", 2]
        goal = ["G", 3]
        out_of_bounds = ["X", -1]

        def char(self):
            return self.value[0]

        def val(self) -> int:
            return self.value[1]

    def __init__(self, size=tuple[int, int], player_location: tuple[int, int] = (0, 0), player_direction: int = 0,
                 goal_location: tuple[int, int] = (-1, -1)):
        # save the size, it will be used later
        if size[0] < 1 or size[1] < 1:
            return
        self.size = tuple(size)
        # the world is a 1d array
        self.world = [self.Tiles.empty] * (self.size[0] * self.size[1])

        self.player = {"location": list(player_location), "dir": player_direction}

        self.world[self.coordinates_to_index(self.player["location"])] = self.Tiles.player

        if goal_location[0] == -1 and goal_location[1] == -1:
            goal_location = (size[0] - 1, size[1] - 1)
        self.goal_location = tuple(goal_location)
        self.world[self.coordinates_to_index(goal_location)] = self.Tiles.goal
        pass

    def step(self):
        return self.__move(0)
        pass

    def get_location_in_direction(self, direction: int = 0) -> list[int]:
        """
        Gets the location of the player in the given direction. Default direction is 0 (forwards)
        :param direction: The direction to get the location in
        :return:
        """
        location = list(self.player["location"])
        if direction == 0:
            location[1] += 1  # location up
        elif direction == 1:
            location[0] += 1  # location right
        elif direction == 2:
            location[1] -= 1  # location down
        elif direction == 3:
            location[0] -= 1  # location left

        return location

    def get_sight(self):
        """
        Gets the player's sight
        :return: What the player sees; -1 = out of bounds, 0 = empty, 1 = wall, 2 = goal
        """
        idx = self.coordinates_to_index(self.get_location_in_direction(self.player["dir"]))

        return self.Tiles.out_of_bounds.val() if idx == -1 else self.world[idx].val()

    def get_location_value(self, location: tuple[int, int]):
        idx = self.coordinates_to_index(location)
        return self.Tiles.out_of_bounds if idx == -1 else self.world[idx]

    # move exists to allow for easier tests, step is the intended function
    def __move(self, direction: int) -> int:
        """
        Moves the player in the given direction
        :param direction: 0 = forwards, 1 = right, 2 = backwards, 3 = left: based on the player's direction
        :return: an integer representing the success or failure of the movement. 0 = success, 1 = failure due to wall,
        2 = failure due to out of bounds, 3 = success due to goal, -1 = failure due to invalid input
        """
        if direction < 0 or direction > 3:
            return -1  # invalid input

        combined_direction = (direction + self.player["dir"]) % 4

        move_location = self.get_location_in_direction(combined_direction)
        # print(f"{move_location = }")

        output = 0

        if not (0 <= move_location[0] < self.size[0] and 0 <= move_location[1] < self.size[1]):
            output = 2  # out of bounds
        world_value = self.get_location_value(move_location)
        if world_value == self.Tiles.wall:
            output = 1  # wall
        elif world_value == self.Tiles.goal:
            output = 3  # goal

        if output == 0 or output == 3:
            # update the world with the new player location
            # set the old player location to empty
            self.world[self.coordinates_to_index(self.player["location"])] = self.Tiles.empty

            # set the new player location to player
            self.world[self.coordinates_to_index(move_location)] = self.Tiles.player

            # update the player's location
            self.player["location"] = move_location

        return output

        pass

    def set_wall(self, location: tuple[int, int]):
        """
        Sets a wall at the given location
        :param location: The location to set the wall
        :return: Returns 0 on success, -1 on failure
        """
        if location == tuple(self.player["location"]):
            return -1
        loc = self.coordinates_to_index(location)
        if loc == -1:
            return -1
        self.world[loc] = self.Tiles.wall
        return 0

    def turn(self, direction: int = 0):
        """
        Turns the player in the given direction
        :param direction: -1 = left, 1 = right
        :return: 0 = success, -1 = failure due to invalid input
        """

        if not (-1 <= direction <= 1):
            return -1
        self.player["dir"] = (self.player["dir"] + direction) % 4
        return 0
        pass

    def to_string(self):
        """
        Generates a string representation of the world
        :return: The string representation of the world
        """
        out = ""
        for i in range(self.size[1] - 1, -1, -1):
            # print(self.world[i * self.size[0]:(i + 1) * self.size[0]])
            for j in self.world[i * self.size[0]:(i + 1) * self.size[0]]:
                out += j.char()
            out += "\n"
        return out

    pass

    def coordinates_to_index(self, coordinates: tuple[int, int] or list[int]) -> int:
        """
        Converts coordinates to an index
        :param coordinates: The coordinates to convert (ints; x, y)
        :return: Returns -1 if the coordinates are invalid, otherwise returns the index (int)
        """
        if type(coordinates) == list and len(coordinates) != 2:
            return -1

        if not (0 <= coordinates[0] < self.size[0] and 0 <= coordinates[1] < self.size[1]):
            # print(f"{coordinates = } (not in range)")
            return -1

        return coordinates[1] * self.size[0] + coordinates[0]
