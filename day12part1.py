from typing import NamedTuple
from itertools import islice, chain
from itertools import repeat
from collections import deque


class Pot(NamedTuple):
    plant: bool
    center: bool = False

    def __str__(self) -> str:
        return "#" if self.plant else "."


class Row(deque):
    def __init__(self, i):
        super(Row, self).__init__(i)

    def transform(self, rule):
        for index, pot in enumerate(self):
            ...
            # if index == 0:
            #     left_items = [Pot(False), Pot(False)]
            #     right_items = islice(self, index + 1, index + 3)
            #     pattern = "".join(
            #         map(str, chain(left_items, [pot], right_items))
            #     )
            #     print(pattern)
            # elif index == 1:
            #     print("Second")
            #     left_items = ["."]
            #     print(index, pot)
            # elif index == len(self) - 2:
            #     print("Second last")
            #     print(index, pot)
            # elif index == len(self) - 1:
            #     print(index, pot)
            #     print("End")
            # else:
            #     print(index, pot)

    def __str__(self):
        return "".join([str(pot) for pot in self])


if __name__ == "__main__":
    with open("input/day12.txt") as f:
        _, _, initial_state = f.readline().split()
        transformations = f.read().strip().splitlines()
        row = Row([Pot(p == "#", i == 0) for i, p in enumerate(initial_state)])
        # Pad with sufficient pots
        row.extendleft(repeat(Pot(False), 3))
        row.extend(repeat(Pot(False), 3))
        print(row)
