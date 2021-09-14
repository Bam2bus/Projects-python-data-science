#!/usr/bin/env python
# coding: utf-8

# In[1]:


namirnice =["jabuke","sok","pršut","pivo"]


# In[2]:


print(namirnice)


# In[3]:


namirnice


# # komentar
# 

# # Stisni M za mark, onda shift+enter da pokrenes kod i da odes u drugu liniju mozes i ALT+Enter

# In[4]:


import pandas as pd


# In[5]:


putnici=pd.read_csv("titanic.csv")


# In[6]:


putnici


# In[7]:


putnici.info()


# # prvih 10 podataka
# 

# In[8]:


putnici.head(10)


# # Zadnjih 10 podataka

# In[9]:


putnici.tail(10)


# In[10]:


putnici.describe()


# # ^^ ovo je za opis arit sredine, min, max itd.

# In[11]:


putnici["Sex"].describe()


# In[12]:


pandas.core.frame.DataFrame


# In[13]:


type(putnici)


# # ^^ tu je pohranjena tablica

# In[14]:


spol=putnici["Sex"]


# In[16]:


type (spol)


# In[17]:


titanik_podskup=putnici[["Sex","Age","Fare"]]


# In[18]:


titanik_podskup.head()


# In[23]:


studenti=pd.read_csv("Students.csv")


# In[24]:


studenti


# In[25]:


studenti.info()


# In[26]:


studenti.describe()


# In[27]:


studenti["race/ethnicity"].describe()


# In[28]:


studenti["race/ethnicity"]


# In[29]:


studenti_podskup=studenti[["gender","race/ethnicity","math score"]]


# In[30]:


studenti_podskup.head(10)


# In[1]:


studenti


# In[3]:


studenti=pd.read_csv("Students.csv")


# In[4]:


import pandas as pd


# In[6]:


studenti=pd.read_csv("Students.csv")


# In[7]:


studenti


# In[8]:


studenti.head()


# In[9]:


studenti.info()


# In[12]:


studenti["gender"].describe()


# In[13]:


studenti["gender"]


# In[14]:


studenti_podskup=studenti[["gender","lunch","math score"]]


# In[15]:


studenti_podskup.info()


# In[16]:


studenti_podskup.describe()


# In[17]:


studenti_podskup.head()


# In[19]:


studenti_podskup.tail()


# # Vjezba 123

# In[ ]:




