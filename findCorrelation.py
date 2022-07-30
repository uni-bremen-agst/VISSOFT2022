#!/usr/bin/env python3
# Calculates the pearson correlations between
# metric, style, architecture violations and LOC.
# Note that SEE.csv must be exported from the
# Axivion Dashboard's Project Index (relevant timestamp: 2021-07-26 11:44:03).
# This script must also be executed in the root folder of SEE.

import csv
import math
from itertools import combinations


def nth(iterable, i):
    return [x[i] for x in iterable]


# mv, sv, av, lines
entries = []

with open("SEE.csv", "r") as csvfile:
    seereader = csv.reader(csvfile, delimiter=';', quotechar='"')
    next(seereader, None)  # skip header
    for file, rev, total, av, cl, cy, de, mv, sv in seereader:
        if int(total) > 0:
            try:
                lines = sum(1 for _ in open(file, "r"))
            except UnicodeDecodeError:
                print(f"Couldn't decode {file}")
                continue
            except FileNotFoundError:
                continue
            entries.append((int(mv), int(sv), int(av), lines))

combos = {0: "MV", 1: "SV", 2: "AV", 3: "LOC"}
# all indices of entries-entries we want to correlate
indices = combinations(range(4), 2)
n = len(entries)
for xi, yi in indices:
    ex = nth(entries, xi)  # entries
    ey = nth(entries, yi)

    ax = sum(ex)/len(ex)  # average
    ay = sum(ey)/len(ey)
    sx = math.sqrt(sum((x - ax)**2 for x in ex) / len(ex))
    sy = math.sqrt(sum((y - ay)**2 for y in ey) / len(ex))
    sxy = sum((e[xi] - ax)*(e[yi] - ay) for e in entries)/len(ex)
    r = sxy/(sx*sy)
    print(f"{combos[xi]} & {combos[yi]}: r = {r}")
