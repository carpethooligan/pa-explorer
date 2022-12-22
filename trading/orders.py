import uuid
import datetime


class Order:
    def __init__(
        self, instrument, tradeDir, orderType, price, size, timestamp, comment
    ) -> None:
        self.orderID = uuid.uuid4()
        self.ocoID = None
        self.parentID = None
        self.direction = tradeDir
        self.orderType = orderType
        self.price = price
        self.size = size
        self.status = "WORKING"
        self.timestamp = timestamp
        self.instrument = instrument
        self.comment = comment

    def __str__(self) -> str:
        return f"Order(instrument={self.instrument},orderDir={self.direction},orderType={self.orderType},price={self.price},size={self.size},orderID={self.orderID},timestamp={self.timestamp})"
