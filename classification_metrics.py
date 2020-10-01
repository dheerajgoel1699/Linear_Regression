# -*- coding: utf-8 -*-
"""Classification metrics

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pOz3fy154qqtT8OIEibwTsXg0pubO7MO

## Classification metrics

Choosing right evaluation metrics for the problem is one of the most important aspect of machine learning. Choice of metrics allows us to compare performance of different models and helps in model selection.

In this task, we will explore following metrics:
- confusion matrix
- accuracy
- precision
- recall
- f1 score

#### Dataset
The training dataset is available at "data/ozone_levels_train.csv" in the respective challenge' repo.<br>
The testing dataset is available at "data/ozone_levels_test.csv" in the respective challenge' repo.<br>

The dataset is __modified version__ of the dataset 'ozone level' on provided by UCI Machine Learning repository.

Original dataset: https://archive.ics.uci.edu/ml/datasets/Ozone+Level+Detection

#### Objective
To learn about classification metrics and compare logistic regression and decision tree on the same dataset

#### Tasks
- define X(input) and Y(output)
- train the decision tree model 
- train the logistic model
- construct a confusion matrix
- calculate the classification accurace
- calculate the Precision
- calculate the Recall
- calculate the F1 score
- calculate Area Under ROC Curve

#### Further fun
- Calculate precission and recall
- find the area under the curve for Roc metrics
- impliment below metrics using inbuilt librarires
        confusion matrix
        accuracy
        precision
        recall
        f1 score


#### Helpful links
- Classification metrics with google developers: https://developers.google.com/machine-learning/crash-course/classification/true-false-positive-negative
- classification metrics: https://www.kdnuggets.com/2020/04/performance-evaluation-metrics-classification.html
- pd.get_dummies() and One Hot Encoding: https://queirozf.com/entries/one-hot-encoding-a-feature-on-a-pandas-dataframe-an-example
- Differences between Logistic Regression and a Decision Tree: https://www.geeksforgeeks.org/ml-logistic-regression-v-s-decision-tree-classification/
- Decision Tree Classifier by Sklearn: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
- Understanding classification metrics like Precision, Recall, F-Scores and Confusion matrices: https://nillsf.com/index.php/2020/05/23/confusion-matrix-accuracy-recall-precision-false-positive-rate-and-f-scores-explained/
- Understanding the ROC Curve: https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
- Use slack for doubts: https://join.slack.com/t/deepconnectai/shared_invite/zt-givlfnf6-~cn3SQ43k0BGDrG9_YOn4g
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import confusion_matrix
# Uncomment below 2 lines to ignore warnings
# import warnings
# warnings.filterwarnings('ignore')

# Download data using wget if running on cloud
!wget https://github.com/DeepConnectAI/challenge-week-5/raw/master/data/ozone_levels_train.csv
!wget https://github.com/DeepConnectAI/challenge-week-5/raw/master/data/ozone_levels_test.csv

# Load the train and test data
train = pd.read_csv("/content/ozone_levels_train.csv")
test  = pd.read_csv("/content/ozone_levels_test.csv")

# Explore train dataset
train

# Explore test dataset
test

# Define X and y
X_train = train.iloc[:,:-1]
X_test  = test.iloc[:,:-1]
y_train = train.iloc[:,-1]
y_test  = test.iloc[:,-1]

# Print shape of X_train, X_test, y_train, y_test
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Initialize the models
# Classifier 1 - Logistic regression
clf1 = LogisticRegression()
# Classifier 2 - Decision tree
clf2 = tree.DecisionTreeClassifier()

# Train both the models on training dataset
n = clf1.fit(X_train, y_train)
m = clf2.fit(X_train, y_train)
print(n)
print(m)

# Predict on testing data
y_pred_lr = clf1.predict(X_test)
y_pred_dt = clf2.predict(X_test)

y_prob_lr = clf1.predict_proba(X_test)
y_prob_dt = clf2.predict_proba(X_test)

"""### Primary building blocks of classification metrics

A __TRUE POSITIVE (TP)__ is an outcome where the model correctly predicts the positive class.

A __TRUE NEGATIVE (TN)__ is an outcome where the model correctly predicts the negative class.

A __FALSE POSITIVE (FP)__ is an outcome where the model incorrectly predicts the positive class.

a __FALSE NEGATIVE (FN)__ is an outcome where the model incorrectly predicts the negative class.
"""

lr_confusion_matrix = confusion_matrix(y_test, y_pred_lr)
print(lr_confusion_matrix)

# Compute primary metrics for logisitc regression
# NOTE: All metrics are to be calculated on test dataset
# True Positive
lr_true_positive = lr_confusion_matrix[0,0]
print(lr_true_positive)
# True Negative
lr_true_negative = lr_confusion_matrix[1,1]
print(lr_true_negative)
# False Positive
lr_false_positive = lr_confusion_matrix[0,1]
print(lr_false_positive)
# False Negative
lr_false_negative = lr_confusion_matrix[1,0]
print(lr_false_negative)

dt_confusion_matrix = confusion_matrix(y_test, y_pred_dt)
print(dt_confusion_matrix)

# Compute primary metrics for decision tree
# True Positive
dt_true_positive = dt_confusion_matrix[0,0]
print(dt_true_positive)
# True Negative
dt_true_negative = dt_confusion_matrix[1,1]
print(dt_true_negative)
# False Positive
dt_false_positive = dt_confusion_matrix[0,1]
print(dt_false_positive)
# False Negative
dt_false_negative = dt_confusion_matrix[1,0]
print(dt_false_negative)

"""### Confusion matrix
A confusion matrix is visualization technique to summarize the basic performance of a classification algorithm.

![Confusion matrix](https://static.packt-cdn.com/products/9781838555078/graphics/C13314_06_05.jpg "Confusion matric diagram")
"""

# Plot confusion matrix, DO NOT EDIT THE CELL
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25,8))

plt.title("Confusion matrix for logistic regression")
sns.heatmap(np.array([[lr_true_negative, lr_false_positive],[lr_false_negative, lr_true_positive]]), annot=True, cmap=plt.cm.Blues, fmt='g', ax=axes[0])
plt.title("Confusion matrix for decision tree")
sns.heatmap(np.array([[dt_true_negative, dt_false_positive],[dt_false_negative, dt_true_positive]]), annot=True, cmap=plt.cm.Blues, fmt='g', ax=axes[1])

plt.show()

"""### Accuracy 
Classification accuracy is simply the rate of correct classifications
$$Accuracy = \frac{Number \, of \, correct \, predictions}{Total \, number \, of \, predictions}$$
<br>
$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
"""

import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score

# Classification accuracy for logistic regression
lr_accuracy = accuracy_score(y_test, y_pred_lr)
# Classification accuracy for decision tree
dt_accuracy = metrics.accuracy_score(y_test, y_pred_dt)

print("Classificaton accuracy: LR = " , lr_accuracy)
print("Classificaton accuracy: DT = " , dt_accuracy)

"""### Precision
What proportion of positive identifications was actually correct?
$$Precision = \frac{TP}{TP+FP}$$
"""

from sklearn.metrics import precision_score

# Precision for logistic regression
try:
    lr_precision = precision_score(y_test, y_pred_lr, average='binary')
except:
    lr_precision = 0
    print("If you see this message, it means that the\ndenominator of precision for logistic regression turned out to be 0 ")
# Precision for decision tree
try:
    dt_precision = precision_score(y_test, y_pred_dt, average='binary')
except:
    dt_precision = 0
    print("If you see this message, it means that the\ndenominator of precision for decision tree turned out to be 0 ")

print("Precision: LR = " , lr_precision)
print("Precision: DT = " , dt_precision)

"""### Recall
What proportion of actual positives was identified correctly?
$$Recall = \frac{TP}{TP+FN}$$
"""

from sklearn.metrics import recall_score

# Recall for logistic regression
try:
    lr_recall = recall_score(y_test, y_pred_lr, average='binary')
except:
    lr_recall = 0
    print("If you see this message, it means that the\ndenominator of recall for logistic regression turned out to be 0 ")
# Recall for decision tree
try:
    dt_recall = recall_score(y_test, y_pred_dt, average='binary')
except:
    dt_recall = 0
    print("If you see this message, it means that the\ndenominator of recall for decision tree turned out to be 0 ")

print("Recall: LR = " , lr_recall)
print("Recall: DT = " , dt_recall)

"""### F1 score
The F1 score can be interpreted as a weighted average of the precision and recall, where an F1 score reaches its best value at 1 and worst score at 0. The relative contribution of precision and recall to the F1 score are equal.
$$ F1 \, score = \frac{2* Precision * Recall}{Precision + Recall}$$
"""

from sklearn.metrics import f1_score

# F1 score for logistic regression
lr_f1_score = f1_score(y_test, y_pred_lr, average='binary')
# F1 score for decision tree
dt_f1_score = f1_score(y_test, y_pred_dt, average='binary')

print("F1 score: LR = " , lr_f1_score)
print("F1 score: DT = " , dt_f1_score)

"""### Area Under ROC Curve
A ROC Curve is a plot of the true positive rate and the false positive rate for a given set of probability predictions at different thresholds used to map the probabilities to class labels. The area under the curve is then the approximate integral under the ROC Curve.
"""

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

# False positive rate & True positive rate for logisitic regression
lr_false_positive_rate, lr_true_positive_rate, thresh1 = roc_curve(y_test, y_prob_lr[:,1], pos_label=1)
# False positive rate & True positive rate for decision tree
dt_false_positive_rate, dt_true_positive_rate, thresh2 = roc_curve(y_test, y_prob_dt[:,1], pos_label=1)

# TODO: Plot the ROC curve
random_probs = [0 for i in range(len(y_test))]
p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)
plt.style.use('seaborn')
plt.plot(lr_false_positive_rate, lr_true_positive_rate, linestyle='--',color='orange', label='Logistic Regression')
plt.plot(dt_false_positive_rate, dt_true_positive_rate, linestyle='-',color='green', label='Decision Tree')
plt.plot(p_fpr, p_tpr, linestyle='-.', color='blue')
plt.title('ROC curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive rate')
plt.legend(loc='best')
plt.show();

#Print ROC-AUC scores for both models
auc_score1 = roc_auc_score(y_test, y_pred_lr)
auc_score2 = roc_auc_score(y_test, y_pred_dt)

print("ROC-AUC Score for Logistic Regression: ",auc_score1)
print("ROC-AUC Score for Decision Tree: ",auc_score2)

