# -*- coding: utf-8 -*-
"""Lab7.ipynb

Automatically generated by Colaboratory.


"""

from google.colab import files
load_data = files.upload()

import sklearn
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

#loading data
dataset = pd.read_csv('mushroom edibility classification dataset.csv')

# missing values
dataset.drop(dataset.columns[dataset.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
dataset.head()

dataset = dataset.dropna(axis = 0, subset = ['cap-shape', 'cap-color'])
  dataset.shape
  print(dataset.info())
  print('unique values in class ' + str(dataset['class'].unique()))
  print('unique values in bruises' + str(dataset['bruises'].unique()))

#encoding categorical features
enc = LabelEncoder()
dataset['class'] = enc.fit_transform(dataset['class'])
dataset['bruises'] = enc.fit_transform(dataset['bruises'])
dataset[['class', 'bruises']].head()

scaler = MinMaxScaler()
scaler.fit(dataset)
dataset_train_scaled = scaler.transform(dataset)
print('per-feature minimum before scaling:\n{}'.format(dataset.min(axis = 0)))
print('per-feature maximum before scaling:\n{}'.format(dataset.max(axis = 0)))
print('per-feature minimum after scaling:\n{}'.format(dataset_train_scaled.min(axis = 0)))
print('per-feature maximum after scaling:\n{}'.format(dataset_train_scaled.max(axis = 0)))

#splitting the dataset into features and labels
features = dataset[['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']]
label = dataset[['class']]
stratified = pd.DataFrame(label)
#8:2 train-test split
xTrain, xTest, yTrain, yTest = train_test_split(features, label, test_size = 0.20, stratify = stratified, random_state = 0)

#using the logistic regression 

perform_logisticRegression = LogisticRegression()
perform_logisticRegression.fit(xTrain, yTrain) 
predictions = perform_logisticRegression.predict(xTest)
accuracy_of_LogisticRegression = accuracy_score(yTest, predictions)
print(accuracy_of_LogisticRegression)

#using the decision tree

perform_decisionTree = DecisionTreeClassifier(criterion='entropy',random_state=1)
perform_decisionTree.fit(xTrain,yTrain)
yPred = perform_decisionTree.predict(xTest)
accuracy_of_DecisionTreeClassifier = accuracy_score(yPred, yTest)
print(accuracy_of_DecisionTreeClassifier)

# comparing the accuracy and plotting them as a bar chart using matplotlib
plt.bar(['Logistic Regression', 'Decision Tree'],[accuracy_of_LogisticRegression, accuracy_of_DecisionTreeClassifier])
plt.title('Comparison between Logistic Regression and Decision Tree' )
plt.show()
