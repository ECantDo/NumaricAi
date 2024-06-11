from thirdAttempt.environment import World


def test_world_init():
    World((1, 1))
    World((0, 0))
    World((-1, -1))


def test_blocked_movement_1x1_up():
    world = World((1, 1))
    assert world.player["location"] == [0, 0]

    # move the player
    assert world.step() == 2  # 2 = failure due to out of bounds
    # the player should be at 0,0
    assert world.player["location"] == [0, 0]


def test_blocked_movement_1x1_down():
    world = World((1, 1), player_direction=2)
    assert world.player["location"] == [0, 0]

    # move the player
    assert world.step() == 2  # 2 = failure due to out of bounds
    # the player should be at 0,0
    assert world.player["location"] == [0, 0]


def test_blocked_movement_1x1_left():
    world = World((1, 1), player_direction=3)
    assert world.player["location"] == [0, 0]

    # move the player
    assert world.step() == 2  # 2 = failure due to out of bounds
    # the player should be at 0,0
    assert world.player["location"] == [0, 0]


def test_blocked_movement_1x1_right():
    world = World((1, 1), player_direction=1)
    assert world.player["location"] == [0, 0]

    # move the player
    assert world.step() == 2  # 2 = failure due to out of bounds
    # the player should be at 0,0
    assert world.player["location"] == [0, 0]


def test_set_wall_1():
    world = World((5, 5))
    assert world.set_wall((0, 1)) == 0

    assert world.get_location_value((0, 1)).val() == 1


def test_set_wall_2():
    world = World((5, 5))
    assert world.set_wall((2, 4)) == 0

    assert world.get_location_value((2, 4)).val() == 1


def test_set_wall_3():
    world = World((5, 5))
    assert world.set_wall((0, 0)) == -1, "That is where the player is located"

    assert world.get_location_value((0, 0)).val() == 2


def test_set_wall_4():
    world = World((5, 5))
    assert world.set_wall((0, -1)) == -1, "Out of bounds"

    assert world.get_location_value((0, -1)).val() == -1


def test_move_up():
    world = World((3, 3), player_location=(1, 1), player_direction=0)
    assert world.step() == 0
    assert world.player["dir"] == 0
    assert world.player["location"] == [1, 2]


def test_move_down():
    world = World((3, 3), player_location=(1, 1), player_direction=2)
    assert world.step() == 0
    assert world.player["dir"] == 2
    assert world.player["location"] == [1, 0]


def test_move_left():
    world = World((3, 3), player_location=(1, 1), player_direction=3)
    assert world.step() == 0
    assert world.player["dir"] == 3
    assert world.player["location"] == [0, 1]


def test_move_right():
    world = World((3, 3), player_location=(1, 1), player_direction=1)
    assert world.step() == 0
    assert world.player["dir"] == 1
    assert world.player["location"] == [2, 1]


def test_blocked_movement_3x3_walls_up():
    world = World((3, 3), player_direction=0)
    assert world.set_wall((0, 1)) == 0

    assert world.step() == 1  # 1 = failure due to wall
    assert world.player["location"] == [0, 0]


def test_blocked_movement_3x3_walls_down():
    world = World((3, 3), player_location=(0, 1), player_direction=2)
    assert world.set_wall((0, 0)) == 0

    assert world.step() == 1  # 1 = failure due to wall
    assert world.player["location"] == [0, 1]


def test_blocked_movement_3x3_walls_left():
    world = World((3, 3), player_location=(1, 0), player_direction=3)
    assert world.set_wall((0, 0)) == 0

    assert world.step() == 1  # 1 = failure due to wall
    assert world.player["location"] == [1, 0]


def test_blocked_movement_3x3_walls_right():
    world = World((3, 3), player_location=(1, 0), player_direction=1)
    assert world.set_wall((2, 0)) == 0

    assert world.step() == 1  # 1 = failure due to wall
    assert world.player["location"] == [1, 0]


def test_turn_right():
    world = World((1, 1), player_direction=0)
    assert world.turn(1) == 0
    assert world.player["dir"] == 1


def test_turn_left():
    world = World((1, 1), player_direction=0)
    assert world.turn(-1) == 0
    assert world.player["dir"] == 3


def test_turn_180_right():
    world = World((1, 1), player_direction=0)
    world.turn(1)
    world.turn(1)
    assert world.player["dir"] == 2


def test_turn_180_left():
    world = World((1, 1), player_direction=0)
    world.turn(-1)
    world.turn(-1)
    assert world.player["dir"] == 2


def test_turn_360_right():
    world = World((1, 1), player_direction=0)
    world.turn(1)
    world.turn(1)
    world.turn(1)
    world.turn(1)
    assert world.player["dir"] == 0


def test_turn_360_left():
    world = World((1, 1), player_direction=0)
    world.turn(-1)
    world.turn(-1)
    world.turn(-1)
    world.turn(-1)
    assert world.player["dir"] == 0


def test_turn_fail_right():
    world = World((1, 1), player_direction=0)
    assert world.turn(2) == -1


def test_turn_fail_left():
    world = World((1, 1), player_direction=0)
    assert world.turn(-2) == -1


def test_sight_out_of_bounds():
    world = World((1, 1))
    assert world.get_sight() == -1


def test_sight_in_bounds():
    world = World((3, 3))
    assert world.get_sight() == 0


def test_sight_wall():
    world = World((3, 3))
    world.set_wall((0, 1))
    assert world.get_sight() == 1


def test_sight_out_of_bounds_turn_left():
    world = World((3, 3))
    assert world.turn(-1) == 0
    assert world.player["dir"] == 3
    assert world.get_sight() == -1


def test_sight_out_of_bounds_turn_right():
    world = World((1, 2))
    assert world.turn(1) == 0
    assert world.player["dir"] == 1
    assert world.get_sight() == -1


def test_sight_goal():
    world = World((3, 3), goal_location=(0, 1))
    assert world.get_sight() == 3


def test_step_on_win():
    world = World((3, 3), goal_location=(0, 1))
    assert world.step() == 3


def test_step_off_win():
    world = World((3, 3), player_location=(0, 1), goal_location=(0, 1))
    assert world.step() == 0

