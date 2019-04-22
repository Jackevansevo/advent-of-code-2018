from dataclasses import dataclass, field
from typing import List

# [TODO] How the fuck do I figure this out?


@dataclass
class Node:
    metadata: List[int]
    children: List["Node"] = field(default_factory=list)


# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----


# A [1,1,2]
# |
# | _ B [10, 11, 12]
# |
# | - C [22]
#     |
#     | - D [99]


if __name__ == "__main__":
    with open("input/day8.txt") as f:
        puzzle_input = [int(n) for n in f.read().strip().split()]
        print(Node.from_line(puzzle_input))
