from itertools import accumulate, cycle
from typing import List


def find_dup_frequency(data: List[str]):
    seen = set()  # type: set
    for freq in accumulate(int(n) for n in cycle(data)):
        if freq in seen:
            return freq
        seen.add(freq)


if __name__ == "__main__":
    with open("input/day1.txt") as f:
        print(find_dup_frequency(f.read().strip().splitlines()))
