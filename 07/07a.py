IN_FILE = "07/input.txt"

if __name__ == "__main__":

    splitters = []
    beams = set()

    with open(IN_FILE) as f:
        for line in f:
            row = []
            for i in range(len(line)):
                if line[i] == "S":
                    beams.add(i)
                    continue
                if line[i] == "^":
                    row.append(i)
            if len(row) > 0:
                splitters.append(row)

    splits = 0
    for row in splitters:
        new_beams = beams.copy()
        for location in row:
            if location in beams:
                new_beams.remove(location)
                new_beams.add(location + 1)
                new_beams.add(location - 1)
                splits += 1
        beams = new_beams

    print(splits)
