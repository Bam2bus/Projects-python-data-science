#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


homes = pd.read_csv ("homeprices.csv")


# In[3]:


homes


# In[4]:


homes.corr()


# In[5]:


plt.xlabel('area')
plt.ylabel('price')
plt.scatter(homes.area,homes.price,color='red',marker='+')


# In[6]:


povrsina = pd.DataFrame(homes["area"])
cijena = pd.DataFrame(homes["price"])


# In[7]:


reg = linear_model.LinearRegression()
model = reg.fit (povrsina, cijena)


# In[8]:


model.coef_


# ### Za svaki square feet cijena ide gore za 135

# In[9]:


model.intercept_


# ### Ako je square feet 0, onda ce cijenia biti 180 616

# In[10]:


model.predict([[3300]])


# ### Kada bi velicina bila 628 715sq feet, cijena bi bila 628 715

# In[11]:


plt.xlabel('area')
plt.ylabel('price')
plt.scatter(homes.area,homes.price,color='red',marker='+')
plt.plot (homes.area, model.predict (homes[["area"]]), color = "blue" )


# In[12]:


new_houses = pd.read_csv("area.csv")


# In[13]:


new_houses


# In[15]:


a = model.predict(new_houses)


# In[16]:


a


# In[17]:


new_houses ["prices"] = a


# In[18]:


new_houses


# ### PRIMJER MATEMATIKA FIZIKA SAMOSTALNO

# In[19]:


matfiz1 = pd.read_csv("matematika_fizika1.csv")


# In[20]:


matfiz1


# In[33]:


matfiz1.corr()


# In[21]:


matfiz2 = pd.read_csv("matematika_fizika2.csv")


# In[22]:


matfiz2


# In[24]:


matematika = pd.DataFrame(matfiz1["matematika"])
fizika = pd.DataFrame(matfiz1["fizika"])


# In[25]:


reg = linear_model.LinearRegression()
model1 = reg.fit (matematika, fizika)


# In[27]:


model1.coef_


# In[28]:


model1.intercept_


# In[29]:


fiz = model1.predict(matfiz2)


# In[31]:


matfiz2 ["fizika"] = fiz


# In[32]:


matfiz2


# In[35]:


plt.xlabel('matematika')
plt.ylabel('fizika')
plt.scatter(matfiz1.matematika,matfiz1.fizika,color='red',marker='+')
plt.plot (matfiz1.fizika, model1.predict (matfiz1[["fizika"]]), color = "blue" )


# In[ ]:




