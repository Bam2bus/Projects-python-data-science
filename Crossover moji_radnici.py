#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[81]:


radnici= pd.read_csv ("moji_radnici.csv")


# In[82]:


radnici.head(35)


# In[83]:


scaler = MinMaxScaler()



scaler.fit(radnici[['average_montly_hours']])
radnici['average_montly_hours'] = scaler.transform(radnici[['average_montly_hours']])


scaler.fit(radnici[['time_spend_company']])
radnici['time_spend_company'] = scaler.transform(radnici[['time_spend_company']])

scaler.fit(radnici[['satisfaction_level']])
radnici['satisfaction_level'] = scaler.transform(radnici[['satisfaction_level']])


# In[84]:


radnici.head()


# In[85]:


X = radnici [["satisfaction_level", "average_montly_hours", "time_spend_company"]]
y = radnici ["left"]


# In[86]:


X.head()


# In[87]:


y.head()


# In[88]:


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 42)


# In[89]:


linreg = linear_model.LinearRegression()
linreg.fit (X_train, y_train)


# In[90]:


linreg.score(X_test, y_test)


# In[91]:


rf = RandomForestRegressor(n_estimators=100, random_state = 0)
rf.fit(X_train, y_train)
rf.score (X_test, y_test)


# In[92]:


lin_scores = cross_val_score(linreg, X, y)


# In[93]:


lin_scores


# In[94]:


lin_scores.mean()


# In[95]:


rf_scores = cross_val_score(rf, X, y)


# In[96]:


rf_scores


# In[97]:


rf_scores.mean()


# In[ ]:




