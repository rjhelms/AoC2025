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
    old_score = 0
    while True:
        new_map = map.copy()
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
                new_map.remove(position)
                score += 1
        if score == old_score:
            break
        map = new_map
        old_score = score

    print(score)
