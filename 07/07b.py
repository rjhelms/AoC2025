from collections import defaultdict
from functools import cache

IN_FILE = "07/input.txt"

SPLITTER_MAP = defaultdict(lambda: None)
MAX_Y = 0


@cache
def find_paths(start_position: tuple[int, int]) -> int:
    position = start_position
    while position[1] < MAX_Y:
        if SPLITTER_MAP[position]:
            return find_paths((position[0] - 1, position[1])) + find_paths(
                (position[0] + 1, position[1])
            )
        else:
            position = (position[0], position[1] + 1)
    return 1


if __name__ == "__main__":

    with open(IN_FILE) as f:
        start_pos = tuple()
        rows = f.readlines()
        MAX_Y = len(rows)
        for y in range(MAX_Y):
            for x in range(len(rows[y])):
                if rows[y][x] == "S":
                    start_pos = (x, y)
                elif rows[y][x] == "^":
                    SPLITTER_MAP[(x, y)] = True

    print(find_paths(start_pos))
