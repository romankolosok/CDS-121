import random
class Stock():
    buyers = []
    def __init__(self, symbol):
        self.__symbol = symbol
        self.prices = []

    @property
    def symbol(self):
        return self.__symbol

    def clear_prices(self):
        self.prices.clear()

    def add_price(self, price):
        '''

        :param price: stock price
        :return:

        this function adds a price of particular stock, list of prices which refers to object(self),
        which has own list of prices and adds this price to it. Since there are lots of stocks, which has his own(unique)
        prices throughout some period of time, they cant be generic for all stocks, which is the reason for list of prices
        to be an object attribute.
        '''
        if not isinstance(price, float):
            raise ValueError("price should be a float number")
        self.prices.append(price)

    @staticmethod
    def avg_float(list_of_floats):
        '''

        :param list_of_floats:
        :return: float number which is average for all ements in the input list

        this function is example of static method in class. It is not referring to any object/class to get variables from it,
        it's just a function which can be used without creating any class instances. We can use it like a regular function,
        pass all arguments and get the result which can be used later
        '''
        return round(sum(list_of_floats) / len(list_of_floats), 2)

    @property
    def low_and_high_price(self):
        return (min(self.prices), max(self.prices))

    @property
    def open_and_close_price(self):
        return (self.prices[0], self.prices[-1])

    def generate_random_prices(self):
        n = random.randint(1, 24)
        for _ in range(n):
            self.add_price(round(random.uniform(10, 1000), 2))

    @classmethod
    def add_customers(cls, *names):
        '''

        :param names: one or couple customer names listed, who bought particular stock this day
        :return:

        we add those customer names to a list of customers, just for example of class methods, it could be better(complicated :) ),
        but I just add them to store everybody, who were buying any stocks

        This function interacts with class attribute (list of strings - buyers), which could be changed from any instance of Stock class
        we can add names to buyers from apple_stock, banana_stock and any object we'll have, this list will be same for
        all objects, since it's an attribute of class itself, that's why we refer to cls.buyers
        '''
        for name in names:
            if isinstance(name, str):
                cls.buyers.append(name)

    @classmethod
    @property
    def customers(cls):
        return cls.buyers


apple_stock = Stock("AAPL")
banana_stock = Stock("BNNA")
tesla_stock = Stock("TSLA")


# print(stock.prices)
# print(stock.avg_stock_price)
# print(stock.low_and_high_price)
# print(stock.open_and_close_price)

apple_stock.add_customers("alan", "david", "neil")
banana_stock.add_customers("daphne, donald")
print(Stock.buyers) #class attribute/method example

apple_stock.add_price(324.567) #object method example
print(apple_stock.prices)


lof = [12.343, 54.653, 67.874, 86.643, 43.3335] #static method example
print(Stock.avg_float(lof))


#Question 1
#We can make attributes "private" just for methods inside it using __ symbol before attribute name when initializing object
#We cant accsess them outside class/object if we will try to refer to it with 'name' or '__name' but python gives up accsess if
#we will use '_className__name' we still can access it, but if those who use or interact the code won't try to use that backdoor
#we can proudly say that our variable 'name' is private






