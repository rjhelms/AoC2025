IN_FILE = "05/input.txt"

if __name__ == "__main__":
    ranges = []
    ingredients = []
    with open(IN_FILE) as f:
        for line in f:
            if len(line) > 1:
                vals = [int(x) for x in line.strip().split("-")]
                if len(vals) == 2:
                    ranges.append(vals)
                else:
                    ingredients.append(vals[0])

    score = 0
    for ingredient in ingredients:
        for range in ranges:
            if ingredient >= range[0] and ingredient <= range[1]:
                score += 1
                break

    print(score)
