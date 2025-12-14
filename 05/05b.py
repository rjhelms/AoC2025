IN_FILE = "05/input.txt"

if __name__ == "__main__":
    ranges = []
    with open(IN_FILE) as f:
        for line in f:
            if len(line) > 1:
                vals = [int(x) for x in line.strip().split("-")]
                if len(vals) == 2:
                    ranges.append(vals)

    ranges.sort()

    while True:
        new_ranges = []
        i = 0
        while i < len(ranges):
            if i + 1 < len(ranges):
                # overlap between ranges - combine them
                if (ranges[i][1] >= ranges[i + 1][0]) and (
                    ranges[i][1] <= ranges[i + 1][1]
                ):
                    new_ranges.append([ranges[i][0], ranges[i + 1][1]])
                    i += 2
                # one range contained within other - keep the larger
                elif (ranges[i][0] <= ranges[i + 1][0]) and (
                    ranges[i][1] >= ranges[i + 1][1]
                ):
                    new_ranges.append(ranges[i])
                    i += 2
                else:
                    new_ranges.append(ranges[i])
                    i += 1
            else:
                new_ranges.append(ranges[i])
                i += 1
        if len(new_ranges) == len(ranges):
            break
        else:
            ranges = new_ranges

    score = 0
    for i in ranges:
        score += i[1] - i[0] + 1

    print(score)
