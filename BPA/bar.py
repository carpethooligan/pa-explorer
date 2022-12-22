from datetime import datetime
import utils


class Bar:
    def __init__(self, barTime, open, high, low, close):
        self.barTime = barTime
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.direction = self.computeDirection()
        self.size = float(self.high) - float(self.low)  # range of whole bar
        if self.high == self.low:
            self.strength = 0
        else:
            self.strength = abs(float(self.open) - float(self.close)) / (
                float(self.high) - float(self.low)
            )

        self.utSize = (
            self.high - self.open if self.isBear else self.high - self.close
        )  # upper tail size
        self.ltSize = (
            self.close - self.low if self.isBear else self.open - self.low
        )  # lower tail size
        self.bodySize = abs(float(self.open) - float(self.close))

    def computeDirection(self):
        if self.isBear:
            return utils.BarDirection.BEAR
        elif self.isBull:
            return utils.BarDirection.BULL
        else:
            return utils.BarDirection.DOJI

    @property
    def isBear(self):
        if self.close < self.open:
            return True
        return False

    @property
    def isBull(self):
        if self.close > self.open:
            return True
        return False

    @property
    def isDoji(self):
        if self.close == self.open:
            return True
        return False

    def __repr__(self) -> str:
        return f"Bar(barTime={repr(self.barTime)},open={self.open},high={self.high},low={self.low},close={self.close})"

    def __eq__(self, other):
        if isinstance(other, Bar):
            return self.barTime == other.barTime

    def __hash__(self) -> int:
        return hash(self.barTime)

    def __lt__(self, other):
        return self.barTime < other.barTime

    def percentSizes(self):
        # calculate tail and body sizes as % of bar's range
        if self.size == 0:
            raise Exception(f"Range is 0 for bar {self.barTime}")

        ut = self.utSize / self.size  # upper tail
        lt = self.ltSize / self.size  # lower tail
        bd = self.bodySize / self.size  # body
        return (ut, lt, bd)

    def percentSameness(self, other):
        # calculate % sameness of tails and bodies between the 2 bars
        if self.utSize == 0 and other.utSize == 0:
            utSameness = 1
        elif self.utSize == 0 or other.utSize == 0:
            utSameness = 0
        else:
            utSameness = (
                self.utSize / other.utSize
                if self.utSize <= other.utSize
                else other.utSize / self.utSize
            )

        if self.ltSize == 0 and other.ltSize == 0:
            ltSameness = 1
        elif self.ltSize == 0 or other.ltSize == 0:
            ltSameness = 0
        else:
            ltSameness = (
                self.ltSize / other.ltSize
                if self.ltSize <= other.ltSize
                else other.ltSize / self.ltSize
            )

        if self.bodySize == 0 and other.bodySize == 0:
            bdSameness = 1
        elif self.bodySize == 0 or other.bodySize == 0:
            bdSameness = 0
        else:
            bdSameness = (
                self.bodySize / other.bodySize
                if self.bodySize <= other.bodySize
                else other.bodySize / self.bodySize
            )

        return (utSameness, ltSameness, bdSameness)

    def percentSimilarToBar(self, other):
        try:

            # calculate averages of tail and body sizes as %'s of bar's range for two bars
            (thisUTP, thisLTP, thisBP) = self.percentSizes()
            (otherUTP, otherLTP, otherBP) = other.percentSizes()

            utAvg = (thisUTP + otherUTP) / 2
            ltAvg = (thisLTP + otherLTP) / 2
            bdAvg = (thisBP + otherBP) / 2

            (utSameness, ltSameness, bdSameness) = self.percentSameness(other)

            # adjusted sameness using weights
            utAdj = utSameness * utAvg
            ltAdj = ltSameness * ltAvg
            bdAdj = bdSameness * bdAvg

            return utAdj + ltAdj + bdAdj
        except:
            pass

        return None
