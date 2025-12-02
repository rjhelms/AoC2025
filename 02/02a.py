IN_FILE = "02/input.txt"

if __name__ == "__main__":
    ranges = []
    score = 0
    with open(IN_FILE) as f:
        str_ranges = [x.split("-") for x in f.read().split(",")]
        for range in str_ranges:
            num_range = []

            # reject ranges that have one odd length
            if len(range[0]) % 2 != 0 and len(range[1]) == len(range[0]):
                continue

            # for lower bound, take starting value or next even length number (eg 1000)
            if len(range[0]) % 2 == 0:
                num_range.append(int(range[0]))
            else:
                num_range.append(10 ** len(range[0]))

            # for upper bound, take starting value or previous even length number (eg 9999)
            if len(range[1]) % 2 == 0:
                num_range.append(int(range[1]))
            else:
                num_range.append(10 ** len(range[0]) - 1)

            ranges.append(num_range)

    for range in ranges:
        test_id = range[0]
        length = len(str(range[0]))
        val = int(str(range[0])[: int(length / 2)])
        test_id = int(str(val) * 2)
        while test_id <= range[1]:
            if test_id >= range[0] and test_id <= range[1]:
                score += test_id
            val += 1
            test_id = int(str(val) * 2)

    print(score)
