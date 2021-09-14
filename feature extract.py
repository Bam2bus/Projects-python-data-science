#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


titanic=pd.read_csv("titanic.csv")


# In[3]:


titanic.head()


# In[5]:


prosjek_cijeneKarte=titanic["Fare"].mean()


# In[6]:


prosjek_cijeneKarte


# In[8]:


titanic["Fare Average"]=(titanic["Fare"]/prosjek_cijeneKarte)


# In[11]:


titanic.head(16)


# In[ ]:




