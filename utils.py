import csv
import os
from dateutil import parser
from datetime import time

# from BPA.bar import Bar
import BPA.bar
from enum import Enum
import pandas as pd

TickSize = 0.25


class OrderType(Enum):
    MARKET = 1
    LIMIT = 2
    STOP = 3


class TradeDirection(Enum):
    FLAT = 0
    LONG = 1
    SHORT = 2


class BarDirection(Enum):
    BULL = 1
    BEAR = 2
    DOJI = 3


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
                    BPA.bar.Bar(
                        barTime,
                        float(row[1]),
                        float(row[2]),
                        float(row[3]),
                        float(row[4]),
                    )
                )
    return bars


def calcEMA(days, prices, emaSpan=20):
    df = pd.DataFrame({"dates": days, "prices": prices})
    df["EMA20"] = df["prices"].ewm(span=emaSpan, adjust=False).mean()

    ema20 = {}
    for row in df.itertuples(index=False):
        ema20[row[0].to_pydatetime()] = row[2]
    return ema20
