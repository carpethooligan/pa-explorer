import csv
import os
from dateutil import parser
from datetime import time
from BPA.bar import Bar


def getAllDataFilenames(dir=None):
    allfilenames = []
    dir = dir or os.walk(os.path.join("data", "ES"))
    for (dirpath, dirnames, filenames) in dir:
        allfilenames.extend(filenames)
        break

    return allfilenames


def getBarsFromDatafile(filepath):
    bars = []
    with open(filepath, newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            barTime = parser.parse(row[0])
            if barTime.time() > time(9, 30, 0) and barTime.time() <= time(16, 15, 0):
                bars.append(
                    Bar(
                        barTime,
                        float(row[1]),
                        float(row[2]),
                        float(row[3]),
                        float(row[4]),
                    )
                )
    return bars
