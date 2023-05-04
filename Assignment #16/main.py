import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import  StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, classification_report, mean_squared_error
from sklearn.svm import SVC



df = pd.read_csv("input.csv")
# print(df)

abc_df = df.iloc[:, :-1]
ans_df = df.iloc[:, -1]
# print(abc_df, ans_df)

X_train, X_test, y_train, y_test = train_test_split(abc_df, ans_df, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# print(X_train, X_test)

pf = PolynomialFeatures(degree=2)
tf = pf.fit_transform(X_train)
X_test_1 = pf.transform(X_test)


linear_reg = LinearRegression().fit(tf, y_train)
# print(linear_reg)
# prediction = linear_reg.predict([[103, 553, 237]])
prediction = linear_reg.predict(X_test_1)
print(prediction)

print(mean_squared_error(y_test, prediction))