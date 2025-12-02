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
        position = (position + move) % 100
        if position == 0:
            score += 1

    print(score)
