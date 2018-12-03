from dataclasses import dataclass, field
from itertools import chain
import re
from typing import Optional, NamedTuple, List


pattern = re.compile(r"\#(\d+)\s@\s(\d+),(\d+)\:\s(\d+)x(\d+)")


@dataclass
class Point:
    x: int
    y: int
    cell: str = field(default=".")
    claims: set = field(default_factory=set)

    def claim(self, claim):
        self.cell = "#"
        self.claims.add(claim.ID)

    def __str__(self) -> str:
        return self.cell


@dataclass
class Fabric:
    # Dimensions
    x: int = field(default=1000)
    y: int = field(default=1000)

    def __post_init__(self):
        self.grid = [
            [Point(x, y) for y in range(self.x)] for x in range(self.y)
        ]

    @property
    def cells(self):
        return chain.from_iterable(self.grid)

    def overlapping(self):
        return len([cell for cell in self.cells if len(cell.claims) >= 2])

    def get_bounds(self, claim) -> List[Point]:
        """Returns flat list of all grid points within the bounds of a claim"""
        return [
            point
            for points in [
                row[claim.left : claim.left + claim.width]
                for row in self.grid[claim.top : claim.top + claim.height]
            ]
            for point in points
        ]

    def draw(self, claim: "Claim") -> List[Point]:
        """
        Marks the points within the bounds of the claim, returns affected cells
        """
        points = self.get_bounds(claim)
        for point in points:
            point.claim(claim)
        return points

    def __str__(self) -> str:
        return "\n".join(
            ["".join([str(cell) for cell in row]) for row in self.grid]
        )


class Claim(NamedTuple):
    ID: int
    left: int
    top: int
    width: int
    height: int

    @staticmethod
    def parse(claim: str) -> Optional["Claim"]:
        """Returns a Claim obj form a str"""
        matches = pattern.match(claim)
        if matches is not None:
            return Claim(*map(int, matches.groups()))
        return None


if __name__ == "__main__":
    with open("input/day3.txt") as f:
        fabric = Fabric()
        for claim in f:
            fabric.draw(Claim.parse(claim))
        print(fabric.overlapping())
