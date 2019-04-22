from day4part1 import grouper, parse_log, match_guards
from operator import attrgetter
from collections import defaultdict, Counter
from itertools import groupby

if __name__ == "__main__":
    with open("input/day4.txt") as f:
        parse_log(f)
        lines = match_guards(sorted(parse_log(f), key=attrgetter("timestamp")))
        grouped_by_guard = groupby(lines, attrgetter("guard"))
        minutes_asleep = defaultdict(Counter)  # type: ignore
        for guard, logs in grouped_by_guard:
            for start, end in grouper(map(attrgetter("timestamp"), logs), 2):
                minutes_asleep[guard].update(range(start.minute, end.minute))

        print(minutes_asleep)
