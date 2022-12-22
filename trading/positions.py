import utils
import traceback


class Positions:
    class Record:
        def __init__(self, instrument, direction, price, amount) -> None:
            self.instrument = instrument
            self.price = price
            self.direction = direction
            self.size = amount if direction == utils.TradeDirection.LONG else -amount

        def __str__(self) -> str:
            return f"Record(instrument={self.instrument},direction={self.direction},price={self.price},position={self.size})"

    def __init__(self) -> None:
        self.records = {}

    def clear(self):
        self.records = {}

    def closeAll(self, instrument, lastPrice):
        netPL = 0
        for inst, pos in self.records.items():

            if inst != instrument:
                continue

            if pos.direction == utils.TradeDirection.LONG:
                netPL += (lastPrice - pos.price) * abs(pos.size)
            else:
                netPL += (pos.price - lastPrice) * abs(pos.size)

        self.clear()
        return netPL

    def update(self, instrument, price: float, direction, amount):
        try:
            if instrument in self.records:
                rec = self.records[instrument]
                rec.price = ((rec.price * abs(rec.size)) + (price * amount)) / 2.0

                if rec.direction == utils.TradeDirection.LONG:
                    if direction == utils.TradeDirection.SHORT:
                        rec.size -= amount
                        if rec.size < 0:
                            rec.direction = utils.TradeDirection.SHORT
                    else:
                        rec.size += amount

                else:
                    if direction == utils.TradeDirection.LONG:
                        rec.size += amount
                        if rec.size > 0:
                            rec.direction = utils.TradeDirection.LONG
                    else:
                        rec.size -= amount

                if rec.size == 0:
                    del self.records[instrument]
                    return None

            else:
                self.records[instrument] = self.Record(
                    instrument, direction, price, amount
                )

            return self.records[instrument]
        except:
            print(traceback.format_exc())
