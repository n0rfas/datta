from core.constants import DirectionTravel


def moving(
    game_map: list[list[object]],
    hero_position: set[int, int],
    direction: DirectionTravel,
):
    match direction:
        case DirectionTravel.UP:
            hero_position[0] -= 1
        case DirectionTravel.DOWN:
            hero_position[0] += 1
        case DirectionTravel.LEFT:
            hero_position[1] -= 1
        case DirectionTravel.RIGHT:
            hero_position[1] += 1

    game_map[hero_position[0]][hero_position[1]].was_visited = True
