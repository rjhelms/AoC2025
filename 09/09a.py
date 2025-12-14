from itertools import combinations

IN_FILE = "09/input.txt"


if __name__ == "__main__":
    tiles = []
    with open(IN_FILE) as f:
        for line in f:
            tiles.append(tuple([int(x) for x in line.split(",")]))

    biggest_area = 0

    for pair in combinations(tiles, 2):
        area = (abs(pair[1][0] - pair[0][0]) + 1) * (abs(pair[1][1] - pair[0][1]) + 1)
        if area > biggest_area:
            biggest_area = area

    print(biggest_area)
