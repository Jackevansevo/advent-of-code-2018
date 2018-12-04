import re
from typing import NamedTuple
from operator import attrgetter, itemgetter
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from itertools import groupby, zip_longest

pattern = re.compile(r"\[(?P<time>.*)\]\s(?:Guard #(?P<id>\d+))*(?P<event>.*)")


class Log(NamedTuple):
    timestamp: str
    event: str
    guard: int


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def parse_log(log):
    for line in log:
        match = pattern.match(line.strip())
        if match:
            timestamp = datetime.strptime(
                match.group("time"), "%Y-%m-%d %H:%M"
            )
            yield Log(timestamp, match.group("event"), match.group("id"))


def match_guards(log):
    for line in log:
        if line.guard is not None:
            guard = line.guard
        else:
            yield Log(line.timestamp, line.event, int(guard))


if __name__ == "__main__":
    with open("input/day4.txt") as f:
        parse_log(f)
        lines = match_guards(sorted(parse_log(f), key=attrgetter("timestamp")))
        grouped_by_guard = groupby(lines, attrgetter("guard"))
        sleep_time = defaultdict(timedelta)  # type: ignore
        minutes_asleep = defaultdict(list)  # type: ignore
        for guard, logs in grouped_by_guard:
            for start, end in grouper(map(attrgetter("timestamp"), logs), 2):
                time_span = end - start
                sleep_time[guard] += time_span
                minutes_asleep[guard] += list(range(start.minute, end.minute))
        most_slept = next(iter(max(sleep_time.items(), key=itemgetter(1))))
        most_minutes = Counter(minutes_asleep[most_slept]).most_common(1)[0][0]
        print(most_slept * most_minutes)
