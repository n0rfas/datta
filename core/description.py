def get_description_of_location(
    game_map: list[list[object]],
    hero_position: set[int, int],
):
    st = game_map[hero_position[0]][hero_position[1]].description

    with open(f'fields_description/{st}.txt', 'r') as file:
        return file.readline()
