import math

IN_FILE = "02/input.txt"

if __name__ == "__main__":
    ranges = []

    with open(IN_FILE) as f:
        str_ranges = [x.split("-") for x in f.read().split(",")]
        for candidate_range in str_ranges:
            int_range = [int(x) for x in candidate_range]
            ranges.append(int_range)

    score = 0

    # use a set so no need to handle duplicates during search
    invalid_ids = set()

    for candidate_range in ranges:

        # determine possible lengths for repeated strings - length divides evenly into
        # either lower or upper bound
        candidate_lengths = []
        for i in range(1, math.floor(len(str(candidate_range[1])) / 2) + 1):
            if (len(str(candidate_range[0])) % i == 0) or (
                len(str(candidate_range[1])) % i == 0
            ):
                candidate_lengths.append(i)

        for length in candidate_lengths:
            # numbers to check are all in that length - could be smarter about this
            # but the search space is still manageable
            min_val = 10 ** (length - 1)
            max_val = 10 ** (length) - 1

            # determine number of times digits could repeat - again, could be
            # smarter. is this only relevant when length == 1?
            min_repeat = math.ceil(len(str(candidate_range[0])) / length)
            max_repeat = math.floor(len(str(candidate_range[1])) / length)

            # hack to avoid single-digit case - damn that sneaky input!
            if min_repeat == 1:
                min_repeat = 2

            for repeats in range(min_repeat, max_repeat + 1):
                for x in range(min_val, max_val + 1):
                    candidate = int(str(x) * repeats)

                    # the one optimization - stop looking once we reach max bounds
                    if candidate > candidate_range[1]:
                        break
                    if candidate >= candidate_range[0]:
                        invalid_ids.add(candidate)

    for id in invalid_ids:
        score += id

    print(score)
