def read_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    node_coord_start = lines.index("NODE_COORD_SECTION\n") + 1
    node_coord_end = lines.index("EOF\n")

    data = []
    for line in lines[node_coord_start:node_coord_end]:
        node_ix, x, y = map(float, line.split(' '))
        data.append((x, y))
    return data


