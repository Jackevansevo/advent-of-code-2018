from day3part1 import Point, Fabric, Claim

if __name__ == "__main__":
    with open("input/day3.txt") as f:
        fabric = Fabric()
        claims = list(filter(None, [Claim.parse(claim) for claim in f]))

        claim_points = dict()

        # Draw all the claims
        for claim in claims:
            claim_points[claim] = fabric.draw(claim)

        for claim, points in claim_points.items():
            if all([len(point.claims) == 1 for point in points]):
                print(claim.ID)
