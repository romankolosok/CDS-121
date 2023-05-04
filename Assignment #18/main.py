import numpy as np
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

mnist = fetch_openml('mnist_784', parser='auto', as_frame=False)

data, labels = mnist.data, mnist.target
labels = labels == '3'

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=.2, random_state=534443, stratify=labels)
sdg = SGDClassifier(random_state=6465)
# sdg.fit(train_data, train_labels)
#
# print(classification_report(test_labels, sdg.predict(test_data)))

predict = cross_val_predict(sdg, train_data, train_labels, cv=5)
print(predict)

cm = confusion_matrix(train_labels, predict)
print(cm)
print(classification_report(train_labels, predict))

# print(train_data)
# def print_digit(digit):
#     '''
#      an entry in this database is a 28x28 bitmap (flattened out to a 784-element list of bytes)
#      To draw it, reshape the array to 28x28 and ask matplotlib to draw.
#     '''
#
#     img = digit.reshape(28,28)
#     plt.imshow(img, cmap="binary")
#     plt.axis('off')
#     plt.show()

# let's look at a random digit to see what's in the data

# print_digit(data[543])
# print(labels[543])