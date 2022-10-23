from datetime import datetime
from .bpautils import Direction


class Bar:
    def __init__(self, barTime, open, high, low, close):
        self.barTime = barTime
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.direction = self.computeDirection()
        self.size = float(self.high)-float(self.low)
        if self.high == self.low:
            self.strength = 0
        else:
            self.strength = abs(float(self.open)-float(self.close)) / (float(self.high)-float(self.low))

    def computeDirection(self):
        if self.isBear:
            return Direction.BEAR
        elif self.isBull:
            return Direction.BULL
        else:
            return Direction.DOJI

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
        return f'Bar(barTime={repr(self.barTime)},open={self.open},high={self.high},low={self.low},close={self.close})'

    def __eq__(self,other):
        if(isinstance(other,Bar)):
            return self.barTime == other.barTime

    def __hash__(self) -> int:
        return hash(self.barTime)

    def __lt__(self, other):
        return self.barTime < other.barTime

