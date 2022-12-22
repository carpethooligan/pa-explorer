import unittest
import datetime
import BPA.bar


class BarTest(unittest.TestCase):
    def setUp(self) -> None:

        self.sut = BPA.bar.Bar(datetime.datetime.now(), 10, 20, 1, 17)
        self.sut2 = BPA.bar.Bar(datetime.datetime.now(), 12, 17, 7, 13)
        return super().setUp()

    def testSizes(self):
        assert self.sut.utSize == 3, "incorrect upper tail size"
        assert self.sut.ltSize == 9, "incorrect lower tail size"
        assert self.sut.bodySize == 7, "incorrect body size"

    def testPercentSizes(self):
        (ut, lt, bd) = self.sut.percentSizes()
        assert ut == 3 / 19, "incorrect upper tail as % of bar's range"
        assert lt == 9 / 19, "incorrect lower tail as % of bar's range"
        assert bd == 7 / 19, "incorrect body size as % of bar's range"

        print(self.sut.percentSimilarToBar(self.sut2))
