import pandas as pd
from pprint import pprint
from matplotlib import pyplot as plt
input_data = pd.read_csv('input.csv')
input_data["First"].plot()
plt.show()
input_data["Second"].plot()
plt.show()
input_data["Third"].plot()
plt.show()
input_data["Fourth"].plot()
plt.show()

pprint(input_data[:].max())