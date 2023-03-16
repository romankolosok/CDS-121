from modules import stocks as stk, exchanges

apple = stk.Stock("AAPL", [123, 424, 421, 123, 13123, 12312, 131])
nvidia = stk.Stock("NVDA", [45345, 464, 64634, 3453, 353, 211, 42353])
intel = stk.Stock("INTL", [423, 212423, 132545, 12242, 243235, 2143255])
sony = stk.Stock("SONY", [4242, 2423, 523423, 2425356, 12324, 356345, 34])

market = exchanges.Exchange("NYMK", [apple, nvidia, intel, sony])
print(market.rising_stocks)

#Main program exists in folder Assignment #11, which is located in folder CDS-121, which is part of the C:\Users\romak\Documents
#Within Assignment #11 folder exists file assignment.py and folder(package with modules) - modules, where 2 files stocks and exchanges are located
#When importing modules from package import uses relative path to the directory modules(since it exists with assignment.py in the same folder),
# when importing stocks to exchange I used '.' to indicate that stocks are in exchange current directory, so python wont throw an error that module doesnt exist