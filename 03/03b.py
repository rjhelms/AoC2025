IN_FILE = "03/input.txt"

TARGET_LENGTH = 12

if __name__ == "__main__":
    battery_strings = []
    with open(IN_FILE) as f:
        for line in f:
            battery_strings.append(line.strip())

    score = 0
    for battery in battery_strings:
        result = 0

        for i in range(TARGET_LENGTH):

            # next digit has to be in range that leaves enough to reach target length
            if TARGET_LENGTH - i - 1 > 0:
                search_string = battery[: -(TARGET_LENGTH - i - 1)]
            else:
                search_string = battery

            # find the highest digit in that range
            best_idx = 0
            best_val = 0
            for j in range(len(search_string)):
                candidate = int(search_string[j])
                if candidate > best_val:
                    best_idx = j
                    best_val = candidate

            # add it to the result
            result *= 10
            result += best_val

            # trim string to everything after chosen digit for next iteration
            battery = battery[best_idx + 1 :]

        score += result
    print(score)
