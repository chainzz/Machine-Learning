# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:04:03 2017

@author: david_boerger
"""

import numpy as np
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

def accuracy_score(truth, pred):
    if len(truth) == len(pred):
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"
    
def predictions(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        if passenger['Sex'] == 'female' or passenger ['Sex'] == 'male' and passenger['Age'] <10:
            if passenger['Sex'] == 'female' and passenger['SibSp'] > 4 or passenger['Sex'] == 'female' and passenger['Age'] > 38 and passenger['Parch'] > 4: 
                predictions.append(0)
            else: 
                predictions.append(1)
        else: predictions.append(0)
    
    return pd.Series(predictions)

# load dataframe
df = pd.read_csv('titanic_data.csv')

outcomes = df['Survived']
df.drop('Survived', axis = 1)

# Make the predictions
Predictions = predictions(df)

print accuracy_score(outcomes, Predictions)
