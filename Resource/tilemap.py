TILE_SIZE = 32

def load_tilemap(path):
    with open(path, "r") as f:
        lines = f.readlines()

    map_data = []
    for line in lines:
        row = [int(char) for char in line.strip()]
        map_data.append(row)
    return map_data
