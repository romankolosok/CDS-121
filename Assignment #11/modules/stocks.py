from dataclasses import dataclass
import typing

@dataclass
class Stock():
    __symbol: str
    prices: typing.List[float]

    @property
    def symbol(self):
        return self.__symbol

    def clear_prices(self):
        self.prices.clear()

    def add_price(self, price):
        if not isinstance(price, float):
            raise ValueError("price should be a float number")
        self.prices.append(price)

    @property
    def avg_stock_price(self):
        return round(sum(self.prices) / len(self.prices), 2)

    @property
    def low_and_high_price(self):
        return (min(self.prices), max(self.prices))

    @property
    def open_and_close_price(self):
        return (self.prices[0], self.prices[-1])


a = Stock("GHFY", [234, 432, 423, 234])