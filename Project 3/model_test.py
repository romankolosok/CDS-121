from joblib import load
from sklearn.metrics import mean_squared_error
import pandas as pd

from get_housing_data import input_data, make_data_cleaning_pipeline, data_prep_pipe, read_dataframe

regressor = load("RFReg.joblib")
data_1, labels_1, data_2, labels_2 = input_data()
data = pd.concat([data_1, data_2], axis=0)
labels = pd.concat([labels_1, labels_2], axis=0)
cleaner = make_data_cleaning_pipeline(data)
data_1_prep = cleaner.transform(data_1)

prep_data = cleaner.transform(data)

print(prep_data)
pred_labels = regressor.predict(prep_data)
pred_labels_1 = regressor.predict(data_1_prep)

print(mean_squared_error(labels, pred_labels, squared=False))
