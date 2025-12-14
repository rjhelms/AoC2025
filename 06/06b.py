IN_FILE = "06/input.txt"


if __name__ == "__main__":
    calculations = []
    with open(IN_FILE) as f:
        lines = f.readlines()
        operator_positions = []

        # idenfity location of operators
        for i in range(len(lines[-1])):
            if lines[-1][i] == "*" or lines[-1][i] == "+":
                operator_positions.append(i)

        # determine operands for each operator
        for i in range(len(operator_positions)):
            position = operator_positions[i]
            calculation = [lines[-1][position]]
            if i < len(operator_positions) - 1:
                end_position = operator_positions[i + 1] - 2
            else:
                end_position = len(lines[-1]) - 1

            # build numbers for each vertical slice
            while position <= end_position:
                number = 0
                for row in range(len(lines) - 1):
                    if lines[row][position] != " ":
                        number *= 10
                        number += int(lines[row][position])
                if number > 0:
                    calculation.append(number)
                position += 1
            calculations.append(calculation)

    score = 0

    for calculation in calculations:
        operator = calculation[0]
        val = 0
        if operator == "*":
            val = 1
        for number in calculation[1:]:
            if operator == "*":
                val *= number
            else:
                val += number
        score += val

    print(score)
