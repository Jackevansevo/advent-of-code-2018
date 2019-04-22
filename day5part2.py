from day5part1 import Polymer


def shortest_polymer(base):
    for letter in set(base.lower()):
        yield len(Polymer.without(base, letter).fully_react())


if __name__ == "__main__":
    with open("input/day5.txt") as f:
        base = f.read().strip()
        print(min(shortest_polymer(base)))
