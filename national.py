# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:38:39 2022

@author: 18329
"""

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df= pd.read_csv("C:\\Users\\18329\\Desktop\\streamlit_deploy\\Preterm.csv")
x= df.iloc[:,:-1]
y = df.iloc[:,-1:]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size= 0.1, random_state=10)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
model = LogisticRegression()
grid={'C':10.0**np.arange(-2,3), 'penalty':['l1','l2']}
cv=KFold(n_splits=5, shuffle=False)
rpj= GridSearchCV(model,grid, cv=cv, n_jobs=-1, scoring='f1_macro')
rpj.fit(x_train,y_train)
from imblearn.under_sampling import RandomUnderSampler
rus= RandomUnderSampler(random_state=1)
x_train_resampled,y_train_resampled = rus.fit_resample(x_train,y_train)
rpj= LogisticRegression(max_iter=1200000).fit(x_train_resampled,y_train_resampled)
y_pred= rpj.predict_proba(x_test)[:,1]
y_pred
import pickle 
filename = 'Pre_term.sav'
pickle.dump(rpj, open(filename, 'wb'))

loaded_model= pickle.load(open('pre_term.sav','rb'))
