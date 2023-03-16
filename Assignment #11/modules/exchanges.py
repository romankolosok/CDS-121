from .stocks import Stock
import typing
from dataclasses import dataclass

@dataclass
class Exchange:
    name: str
    stocks: typing.List[Stock]

    def remove_stock(self, name):
        for i in range(len(self.stocks)):
            if self.stocks[i].symbol == name:
                del self.stocks[i]
                break
        else:
            raise ValueError("no stock with this name was found")


    def add_stock(self, symbol, *prices):
        if isinstance(prices[0], list):
            self.stocks.append(Stock(symbol, prices[0]))
        else:
            self.stocks.append(Stock(symbol, list(prices)))

    @property
    def rising_stocks(self):
        res_list = []
        for stock in self.stocks:
            if stock.open_and_close_price[1] - stock.open_and_close_price[0] > 0:
                res_list.append(stock)
        return res_list
