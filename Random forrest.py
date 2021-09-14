#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# In[2]:


cvijece = pd.read_csv ("moj_iris.csv")


# In[3]:


cvijece.head()


# In[4]:


cvijece.drop(['Unnamed: 0'], axis = 1, inplace = True)


# In[5]:


cvijece.head()


# In[6]:


X=cvijece[['sepal length', 'sepal width', 'petal length', 'petal width']]
y=cvijece['species']


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 10)


# In[8]:


clf=RandomForestClassifier(n_estimators=25)


# In[9]:


clf.fit(X_train,y_train)


# In[10]:


y_pred=clf.predict(X_test)


# In[11]:


y_pred


# In[12]:


score = clf.score(X_test, y_test)


# In[13]:


score


# ## Feature importance

# In[14]:


feature_imp = pd.DataFrame(clf.feature_importances_, index=X_train.columns, columns=
['importance']).sort_values('importance', ascending=False)


# In[15]:


feature_imp


# ## Gledamo koji su featuri dominantniji

# In[16]:


X=cvijece[['sepal length', 'petal length', 'petal width']]
y=cvijece['species']


# In[17]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 10)


# In[18]:


clf=RandomForestClassifier(n_estimators=25)


# In[19]:


clf.fit(X_train,y_train)


# In[20]:


y_pred=clf.predict(X_test)


# In[21]:


y_pred


# In[22]:


score = clf.score(X_test, y_test)


# In[23]:


score


# In[ ]:




