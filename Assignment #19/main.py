import numpy as np
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.multiclass import OneVsRestClassifier
from joblib import load, dump

mnist = fetch_openml('mnist_784', parser='auto', as_frame=False)

data, labels = mnist.data, mnist.target
# labels = labels == '3'

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=.2, random_state=534443, stratify=labels)
sdg = SGDClassifier(random_state=6465)
rfc = RandomForestClassifier(random_state=6465, n_jobs=-1)
# ovr_rfc = OneVsRestClassifier(rfc).fit(train_data, train_labels)
# dump(ovr_rfc, "random_classifier.joblib")
ovr_rfc = load("random_classifier.joblib")
prediction = ovr_rfc.predict(test_data)

print(train_labels[2])
print(ovr_rfc.predict([train_data[2]]))

# sdg.fit(train_data, train_labels)
#
# print(classification_report(test_labels, sdg.predict(test_data)))

# predict = cross_val_predict(sdg, train_data, train_labels, cv=5)
# print(predict)
#
cm = confusion_matrix(test_labels, prediction)
print(cm)
print(classification_report(test_labels, prediction))
