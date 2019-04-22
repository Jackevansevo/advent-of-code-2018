import collections


def opposite_polarity(x, y):
    return y.islower() if x.isupper() else y.isupper()


def same_type(x, y):
    return x.lower() == y.lower()


def tail(n, iterable):
    "Return an iterator over the last n items"
    # tail(3, 'ABCDEFG') --> E F G
    return iter(collections.deque(iterable, maxlen=n))


class Polymer:
    def __init__(self, poly):
        self.poly = poly

    @classmethod
    def without(cls, poly, letter):
        removed = "".join([s for s in poly if s.lower() != letter])
        return cls(removed)

    def react(self):
        for index, l in enumerate(self.poly):
            if index != len(self.poly) - 1:
                n = self.poly[index + 1]
                if same_type(l, n) and opposite_polarity(l, n):
                    return self.poly[:index] + self.poly[index + 2 :]

    def fully_react(self):
        return next(tail(1, self))

    def __iter__(self):
        return self

    def __next__(self):
        new_polymer = self.react()
        if new_polymer is not None and new_polymer != self.poly:
            self.poly = new_polymer
            return new_polymer
        else:
            raise StopIteration


if __name__ == "__main__":
    with open("input/day5.txt") as f:
        polymer = Polymer(f.read().strip())
        print(len(polymer.fully_react()))
