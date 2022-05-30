import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# function to predict marks

def marks_pred(marks):

    # reading the dataset and storing it in a pandas series
    df = pd.read_csv('Linear Regression - Sheet1.csv')

    # spliting the dataset into inputs and targets

    X=df['X']
    Y=df['Y']

    # reshaping the inputs

    X=X.to_numpy()
    X=X.reshape(-1, 1)

    # training the model

    model = LinearRegression()
    model.fit(X,Y)

    # prediction with the model

    X_test=np.array(marks)
    X_test=X_test.reshape((-1,1))

    return model.predict(X_test)

