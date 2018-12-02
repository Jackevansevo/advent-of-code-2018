from itertools import combinations
from operator import eq


def find_id(data):
    for x, y in combinations(data, 2):
        # Find the index of every mismatched character in each combination pair
        diff = [i for i, d in enumerate(zip(x, y)) if not eq(*d)]
        if len(diff) == 1:
            diff_char_index = next(iter(diff))
            yield x[:diff_char_index] + x[diff_char_index + 1 :]


if __name__ == "__main__":
    with open("input/day2.txt") as f:
        data = f.read().splitlines()
        print(next(find_id(data)))
