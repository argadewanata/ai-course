#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
import sys
sys.path.append("../tools/")
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from email_preprocess import preprocess
from time import time


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
clf = SVC(kernel="linear")
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print(f"Accuracy: {acc}")

# Reduce the data to 2D using PCA for visualization
pca = PCA(n_components=2)
X_2d = pca.fit_transform(features_train)

# Create a mesh grid for the decision boundary
h = 0.02  # Step size in the mesh
x_min, x_max = X_2d[:, 0].min() - 1, X_2d[:, 0].max() + 1
y_min, y_max = X_2d[:, 1].min() - 1, X_2d[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predict labels for each point in the mesh
Z = clf.predict(pca.inverse_transform(np.c_[xx.ravel(), yy.ravel()]))

# Reshape the prediction to match the mesh shape
Z = Z.reshape(xx.shape)

# Plot the decision boundary and support vectors
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels_train,
            cmap=plt.cm.coolwarm, marker='x')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('SVM Decision Boundary')
plt.show()

#########################################################

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''

# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

#########################################################
