from collections import defaultdict

DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

IN_FILE = "04/input.txt"

if __name__ == "__main__":
    map = []
    with open(IN_FILE) as f:
        data = f.read().splitlines()
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == "@":
                    map.append((x, y))

    score = 0
    for position in map:
        adjacent = 0
        for check_offset in DIRECTIONS:
            check_location = (
                position[0] + check_offset[0],
                position[1] + check_offset[1],
            )
            if check_location in map:
                adjacent += 1
        if adjacent < 4:
            score += 1

    print(score)
