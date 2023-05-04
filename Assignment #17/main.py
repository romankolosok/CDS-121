import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import numpy as np
df = pd.read_csv("housing.csv")

train, test = train_test_split(df, test_size=0.2, random_state=124124)
train_labels = train['median_house_value']
test_labels = test['median_house_value']
train.drop(columns=['median_house_value', 'longitude', 'latitude'], axis=1, inplace=True)
test.drop(columns=['median_house_value', 'longitude', 'latitude'], axis=1, inplace=True)

# print(train, test)

num_pipeline = Pipeline(steps=[
    ("impute", SimpleImputer(strategy="median")),
    ("standardize", StandardScaler()),
])

cat_pipeline = Pipeline(steps=[
    ("encoder", OneHotEncoder(sparse_output=False))
])

preprocess = ColumnTransformer([
    ('num_pipeline', num_pipeline, ['housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income']),
    ('cat_pipeline', cat_pipeline, ['ocean_proximity'])
])


#training preprocessor pipeline for train data
preprocess.fit(train)
reg = LinearRegression()
prep_train = preprocess.transform(train)
reg.fit(prep_train, train_labels)

predictions_1 = reg.predict(prep_train)#predicting for itself
prep_test = preprocess.transform(test)
predictions_2 = reg.predict(prep_test)#predicting for test data
# see how predictions compare to train_labels
print(mean_squared_error(train_labels, predictions_1) ** 0.5)
print(mean_squared_error(test_labels, predictions_2) ** 0.5)

