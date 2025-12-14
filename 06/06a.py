IN_FILE = "06/input.txt"

if __name__ == "__main__":
    number_rows = []
    operations = []
    with open(IN_FILE) as f:
        for line in f:
            line = line.split()
            if line[0] == "*" or line[0] == "+":
                operations = line
            else:
                number_rows.append([int(x) for x in line])

    score = 0

    for i in range(len(operations)):
        operation = operations[i]
        if operation == "*":
            val = 1
        else:
            val = 0
        for row in number_rows:
            if operation == "*":
                val *= row[i]
            else:
                val += row[i]
        score += val

    print(score)
