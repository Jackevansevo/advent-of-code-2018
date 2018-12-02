from collections import Counter

if __name__ == "__main__":
    with open("input/day2.txt") as f:
        data = f.read().splitlines()
        occurances = [Counter(d).values() for d in data]
        twice, trice = [[o for o in occurances if n in o] for n in (2, 3)]
        print(len(trice) * len(twice))
