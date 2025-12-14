from itertools import combinations

IN_FILE = "08/input.txt"


def calc_distance(box_1: tuple[int, int, int], box_2: tuple[int, int, int]) -> int:
    distance = 0
    for i in range(3):
        distance += (box_1[i] - box_2[i]) ** 2
    return distance


if __name__ == "__main__":
    boxes = []
    circuits = []
    with open(IN_FILE) as f:
        for line in f:
            boxes.append(tuple(int(x) for x in line.split(",")))

    # calculate distance for every pair of boxes
    combinations_dict = {}
    for box_pair in combinations(boxes, 2):
        combinations_dict[(box_pair[0], box_pair[1])] = calc_distance(
            box_pair[0], box_pair[1]
        )

    sorted_combinations = sorted(
        combinations_dict, key=combinations_dict.get, reverse=True
    )

    while True:
        # grab closest remaining pair of boxes
        this_pair = sorted_combinations.pop()

        # find all the circuits that contain one of the pair
        circuits_to_join = []
        for circuit in circuits:
            if this_pair[0] in circuit or this_pair[1] in circuit:
                circuits_to_join.append(circuit)

        if len(circuits_to_join) == 0:
            # if none, create a new circuit
            circuits.append(set(this_pair))
        else:
            # otherwise, merge all the found circuits, and add the new pair
            new_circuit = set()
            for circuit in circuits_to_join:
                new_circuit = new_circuit.union(circuit)
                circuits.remove(circuit)
            new_circuit = new_circuit.union(set(this_pair))

            # for part 2 - go until the new circuit contains every box
            if len(new_circuit) == len(boxes):
                print(this_pair[0][0] * this_pair[1][0])
                break
            circuits.append(new_circuit)
