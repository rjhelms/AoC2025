IN_FILE = "03/input.txt"

if __name__ == "__main__":
    battery_dicts = []

    with open(IN_FILE) as f:
        for line in f:
            this_battery = {}
            for i in range(10):
                this_battery[i] = []
            for idx in range(len(line.strip())):
                this_battery[int(line[idx])].append(idx)
            battery_dicts.append(this_battery)

    score = 0
    for battery in battery_dicts:
        found_val = None
        for i in range(9, 0, -1):
            if found_val:
                break
            if len(battery[i]) > 0:
                min_i_idx = battery[i][0]
                for j in range(9, 0, -1):
                    if len(battery[j]) > 0:
                        for idx in battery[j]:
                            if idx > min_i_idx:
                                found_val = i * 10 + j
                                break
                    if found_val:
                        break
        score += found_val

    print(score)
