IN_FILE = "01/input.txt"

if __name__ == "__main__":
    score = 0
    moves = []
    position = 50
    with open(IN_FILE) as f:
        for line in f:
            if line[0] == "L":
                moves.append(-int(line[1:]))
            else:
                moves.append(int(line[1:]))

    for move in moves:
        # for moves that are greater than one full rotation, knock off the full rotations
        while move > 100:
            score += 1
            move -= 100
        while move < -100:
            score += 1
            move += 100

        position = position + move

        # count when crossed either bound, or ended at zero
        # and catch case where move *started* at zero
        if (position < 0 or position > 99 or position == 0) and position != move:
            score += 1

        position = position % 100

    print(score)
