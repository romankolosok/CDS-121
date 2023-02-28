import random
from dataclasses import dataclass

class Stock():
    buyers = []
    def __init__(self, symbol):
        self.__symbol = symbol
        self.prices = []

    def __eq__(self, other):
        return self.__symbol == other.__symbol

    def __gt__(self, other):
        return self.__symbol > other.__symbol

    def __lt__(self, other):
        return self.__symbol < other.__symbol

    def __ge__(self, other):
        return self.__symbol >= other.__symbol

    def __le__(self, other):
        return self.__symbol <= other.__symbol

    def __str__(self):
        return f"Stock symbol: '{self.__symbol}', Stock prices: {', '.join(self.prices)}"

    def __repr__(self):
        return f"Stock(symbol={self.__symbol!r})"

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

banana_stock = Stock("BNNA")
apple_stock = Stock("AAPL")
apple = Stock("AAPL")
# print(banana_stock > apple_stock)
print(apple_stock.__str__(), apple_stock.__repr__())


tesla_stock = Stock("TSLA")

#duck typing example
#duck typing is when functionality of same method works differently depending on object it's in.
# If it quacks like a duck(has quacking method) and look like a duck(child of duck) then it's a duck :)
class Dish:
    def __init__(self, *ingredients):
        self.ingredients = list(ingredients)

    def mix_it(self, mixin_1, mixin_2):
        print(f"Mix {mixin_1} with {mixin_2}")

    def swirl_it(self, mixin_1, mixin_2):
        print(f"Swirl {mixin_1} and {mixin_2}")

    def cook_it(self):
        self.mix_it(self.ingredients[0], self.ingredients[-1])

class Soup(Dish):
    def cook_it(self):
        self.swirl_it(self.ingredients[1], self.ingredients[-1])
        self.mix_it(self.ingredients[0], "salt")

class Crepe(Dish):
    def cook_it(self):
        self.swirl_it("flour", "milk")
        self.mix_it(self.ingredients[0], self.ingredients[-1])
        self.mix_it("eggs", "sugar")


crepe_with_cottage_cheese = Crepe("cottage cheese", "vanilla sugar")
print("\nCrepe recipe:")
crepe_with_cottage_cheese.cook_it()

pho = Soup("beef broth", "noodles", "beef")
print("\nPho recipe:")
pho.cook_it()





