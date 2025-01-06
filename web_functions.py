import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#nyimpen data yg ngambil dari code model
@st.cache_data
def load_data():
    
    iris = pd.read_csv("Iris.csv")

    X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    y = iris['Species']

    return iris, X, y


@st.cache_data
def train_model_DT(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    
    # membuat model Decision Tree
    tree_model = DecisionTreeClassifier()

    # melakukan pelatihan model terhadap data
    tree_model = tree_model.fit(X_train, y_train)

    y_pred = tree_model.predict(X_test)

    acc_score = round(accuracy_score(y_pred, y_test), 3)

    return tree_model, acc_score


@st.cache_data
def predict_DT(x, y, features):
    tree_model, acc_secore = train_model_DT(x, y) # type: ignore

    predict = tree_model.predict(np.array(features).reshape(1, -1))

    return predict, acc_secore


@st.cache_data
def train_model_KNN(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=5)
    knn = KNeighborsClassifier(n_neighbors=12)
    knn = knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    acc_score = metrics.accuracy_score(y_test, y_pred)

    return knn, acc_score


@st.cache_data
def predict_KNN(x, y, features):
    knn, acc_score = train_model_KNN(x, y)

    predict = knn.predict(np.array(features,dtype=np.float64).reshape(1,-1))

    return predict, acc_score


@st.cache_data
def train_model_NBC(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)
    gaussian = GaussianNB()
    nbc = gaussian.fit(X_train, y_train)
    Y_pred = gaussian.predict(X_test)
    acc_score = round(accuracy_score(y_test, Y_pred) * 100, 2)
    acc_gaussian = round(gaussian.score(X_train, y_train) * 100, 2)

    cm = confusion_matrix(y_test, Y_pred)
    precision = precision_score(y_test, Y_pred, average='micro')
    recall = recall_score(y_test, Y_pred, average='micro')
    f1 = f1_score(y_test, Y_pred, average='micro')

    return nbc, acc_score, acc_gaussian, precision, recall, f1,cm


@st.cache_data
def predict_NBC(x, y, features):
    nbc, acc_score = train_model_KNN(x, y)

    predict = nbc.predict(np.array(features,dtype=np.float64).reshape(1, -1))

    return predict, acc_score



    
