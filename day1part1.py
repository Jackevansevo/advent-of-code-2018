if __name__ == "__main__":
    with open("input/day1.txt") as f:
        print(sum([int(n) for n in f.read().strip().splitlines()]))
