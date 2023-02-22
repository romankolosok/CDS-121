import random
import matplotlib.pyplot as plt
import numpy as np
class Stock():
    def __init__(self, symbol):
        self.symbol = symbol
        self.prices = []

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


stock = Stock("AAPL")
n = random.randint(1,24)
for _ in range(n):
    stock.add_price(round(random.uniform(10,1000), 2))

print(stock.prices)
print(stock.avg_stock_price)
print(stock.low_and_high_price)
print(stock.open_and_close_price)

#simple matplot usage
plt.rcParams['figure.dpi']=400
plt.title("Stock prices during day")
plt.ylabel("Price, $")
plt.xlabel("Hour, hr")
plt.grid()

plt.bar(np.linspace(1, n, n) ,stock.prices, edgecolor='black', linewidth=1, color='green')

plt.show()

