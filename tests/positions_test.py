import unittest
from trading.positions import Positions
from utils import TradeDirection

# Test Updating Positions
class Update(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = Positions()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def testAddNewPosition(self):
        self.sut.update("ES", "123.45", TradeDirection.LONG, 1)
        assert (
            len(self.sut.records) == 1
        ), "incorrect number of positions when adding new"

        assert self.sut.records["ES"].instrument == "ES", "incorrect instrument"
        assert self.sut.records["ES"].price == "123.45", "incorrect price"
        assert (
            self.sut.records["ES"].direction == TradeDirection.LONG
        ), "incorrect direction"
        assert self.sut.records["ES"].size == 1, "incorrect size"
