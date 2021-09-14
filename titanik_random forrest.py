#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# In[2]:


titanik = pd.read_csv ("titanic.csv")


# In[3]:


titanik.head()


# ## Categorical data encoding

# In[4]:


gender_clean = {"Sex" : {"male" : 1, "female" : 0}}


# In[5]:


gender_clean


# In[6]:


titanik.replace(gender_clean, inplace=True)


# In[7]:


titanik.head(15)


# # Random forrest

# In[ ]:




