#!/usr/bin/env python3
# Calculates the solutions for the dashboard exercises.
# Note that SEE.csv must be exported from the
# Axivion Dashboard's Project Index (relevant timestamp: 2021-07-26 11:44:03).
# This script must also be executed in the root folder of SEE.
import csv
from collections import defaultdict

# format: (file, area, lines, issues)
entries = []

with open("SEE.csv", "r") as csvfile:
    seereader = csv.reader(csvfile, delimiter=';', quotechar='"')
    next(seereader, None)  # skip header
    for file, rev, total, av, cl, cy, de, mv, sv in seereader:
        if file.count('/') != 3 or not file.startswith("Assets/SEE/"):
            continue
        try:
            lines = sum(1 for _ in open(file, "r"))
        except UnicodeDecodeError:
            print(f"Couldn't decode {file}")
            continue
        except FileNotFoundError:
            continue
        issues = {"AV": int(av), "CL": int(cl),
                  "CY": int(cy), "DE": int(de),
                  "MV": int(mv), "SV": int(sv)}
        entries.append((file.split('/')[3], file.split('/')[2], lines, issues))

entries.sort(key=lambda x: (x[1], x[2]), reverse=True)

counted: defaultdict = defaultdict(lambda: 0)
currentone = ""
for entry in entries:
    counted[entry[1]] += 1
    if counted[entry[1]] > 5:
        continue
    if currentone != entry[1]:
        currentone = entry[1]
        print(f"\n{entry[1]}:")
    print(f"{entry[0]} ({entry[2]}) : {entry[3]}")
