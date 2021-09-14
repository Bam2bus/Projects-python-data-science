#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


turisti=pd.read_excel("Turisti.xlsx")


# In[3]:


turisti.head()


# In[4]:


turisti.describe()


# In[5]:


turisti.info()


# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


plt.hist (turisti.Price, bins = 15)
plt.xlabel("Cijena")
plt.ylabel ("Broj turista")
plt.title ("Broj dana po cijeni")


# In[8]:


turisti.plot(kind="scatter", x="Price", y="NoDays")


# ## Cijena po broju dana provedenih u apartmanu vidimo jedan outlier, nevjerujem da je 10 dana boravka u nekom apartmanu 175000, ispod ˇˇ se vidi da je to Padova

# In[9]:


turisti.loc [turisti["Price"] >=150000, ["Country","City","NrPeople","Price","Service"]]


# In[10]:


cijena_mean=turisti["Price"].mean()


# In[11]:


cijena_mean


# In[12]:


cijena_std=turisti["Price"].std()


# In[13]:


cijena_std


# In[14]:


turisti["zscore_cijena"]=(turisti["Price"]-cijena_mean)/cijena_std


# In[15]:


turisti


# In[16]:


turisti[turisti["zscore_cijena"]<3]


# In[17]:


turisti_copy2=turisti[turisti["zscore_cijena"]<3]


# ## Korištenjem zscore za micanje outliera vidimo da postoje 2 koja su veća od 3 koji je granica

# In[18]:


turisti[turisti["zscore_cijena"]>-3]


# ## Za -3 ima samo 1 outlier

# In[19]:


turisti.duplicated().sum()


# ## Prema ovome podatku možemo vidjeti da ima 15 duplikata

# In[20]:


turisti[turisti.duplicated(keep=False)]


# ## Ako maknemo duplikate imamo 293 retka

# In[21]:


turisti.drop_duplicates(inplace=True)


# In[22]:


turisti.duplicated().sum()


# ## Sa gornjim dijelom koda smo maknuli sve duplikate

# In[23]:


turisti.isna().sum()


# In[24]:


turisti.loc[turisti.isnull().any(axis=1)]


# In[25]:


turisti ["Country"].fillna("Španjolska", inplace=True)


# In[26]:


turisti.loc[turisti.isnull().any(axis=1)]


# In[27]:


turisti_copy=turisti


# In[28]:


turisti_copy.dropna(how = "any", thresh=3, inplace = True)


# In[29]:


turisti_copy


# In[30]:


turisti_copy.loc[turisti.isnull().any(axis=1)]


# ## Proba za dropanje Italije

# In[31]:


turisti.dropna(how = "any", thresh=3, inplace = True)


# In[32]:


turisti.loc[turisti.isnull().any(axis=1)]


# In[33]:


turisti.loc [turisti["Country"] =="Španjolska", ["Country","City","NrPeople","Price","Motivation","NoDays"]]


# In[34]:


turisti ["City"].value_counts()


# In[35]:


turisti ["City"].fillna("Barcelona", inplace=True)


# ## Stavio sam Barcelonu jer je više posjećivana od Madrida, no da sam stavio i Madrid ne bi promašio

# In[36]:


turisti.loc[turisti.isnull().any(axis=1)]


# In[37]:


turisti ["Motivation"].value_counts()


# In[38]:


turisti ["Motivation"].fillna("tourism", inplace=True)


# ## Stavio sam turizam jer po broju se vidi da većina dolazi u Madrid turistički

# In[39]:


turisti.loc[turisti.isnull().any(axis=1)]


# In[40]:


turisti ["NrCh"].value_counts()


# In[41]:


turisti ["NrCh"].fillna("0.0", inplace=True)


# ## Stavio sam nulu jer je motivacija poslovno putovanje, mislim da niko ne vodi djecu na poslovno putovanje

# In[42]:


turisti.loc[turisti.isnull().any(axis=1)]


# In[43]:


turisti ["Transport"].value_counts()


# In[44]:


turisti ["Transport"].fillna("airplane", inplace=True)


# ## Avion je iz razloga da čisto sumnjam da je dosao busem ili tramvajem do Reykjavika, da postoji brod kao opcija dalo bi se rasmišljat

# In[45]:


turisti.loc[turisti.isnull().any(axis=1)]


# In[46]:


turisti_španjolska=turisti.loc [turisti ["Country"] == "Španjolska" , ["NrPeople"]]


# In[47]:


turisti_španjolska.mean()


# In[48]:


turisti ["NrPeople"].fillna(3.0, inplace=True)


# ## Stavljeno je 3 ljud iz razloga što nije moguće da putuje 3.23 čovijeka

# In[49]:


turisti.loc[turisti.isnull().any(axis=1)]


# In[50]:


turisti["City"].replace({"rome": "Rome"}, inplace=True)


# In[51]:


turisti ["City"].value_counts()


# In[78]:


turisti["Motivation"].replace({"busines": "business"}, inplace=True)


# In[53]:


turisti ["Motivation"].value_counts()


# In[54]:


turisti["NrCh"].replace({222.0:2.0}, inplace=True)


# In[55]:


turisti ["NrCh"].value_counts()


# In[56]:


turisti["Transport"].replace({"Airplane": "airplane"}, inplace=True)


# In[57]:


turisti ["Transport"].value_counts()


# In[58]:


turisti ["Country"].value_counts()


# In[59]:


turisti ["NoDays"].value_counts()


# In[60]:


turisti ["NrPeople"].value_counts()


# In[61]:


turisti ["Loyalty"].value_counts()


# In[62]:


turisti ["Paymenttype"].value_counts()


# In[63]:


turisti.corr()


# ## Korelacija ili veze između podataka u tablici kao što možemo vidjeti većina nema korelaciju, no broje ljudi i broj djece su u vezi jer vjerovatno jer ako neki par ide sa djecom i ona se upisuju ko putnici i samim time dodaje se kao broj ljudi na putovanju

# In[64]:


import seaborn as sns


# In[65]:


turisti.info()


# In[66]:


fig = plt.figure()
sns.boxplot(x="Country", y="Price", data=turisti_copy2)


# In[80]:


fig = plt.figure()
sns.boxplot(x="Motivation", y="Price", data=turisti_copy2)


# ## Prema podacima iz ova 2 grafa, jedan je za cijenu i za državu, gledajući njega imamo podatak da bi Island bio najskuplji, te vidimo da Francuska i Portugla isto imaju najveću cijenu karte ili ukupnih karata od 2500, Portugalu je median oko 2250, ali Francuskoj je oko 1750, sad najefeftinija ili najmanja cijena karte pripada Italiji, koja mi mogla biti oko 200

# ## Drugi graf prikazuje vezu između motivacije i cijene, cini se da je median ili prosjek cijene za turizam 1700, a najveća bi mogla biti oko 3000, namjanja bi bila 800
# ## Za poslovno putovanje najmanja je 800, najveća je 1400, dok je prosjek 1200
# ## Samim time mozemo zakljuciti da se agencija najviše koristi za turisticka putovanja nego za poslovna
# 

# In[68]:


turisti_copy2 ["Price"].agg (["count","min","max","mean"])


# In[69]:


turisti_class=turisti_copy2.groupby(["Country","City","Motivation"])


# In[70]:


turisti_class ["Price"].max()


# ## Podaci su grupirani prema državi, gradu i motivaciji dolaska u područje, kao što vidimo uzeo sam cijenu i da mi da najveću cijenu za određeni grad te motivaciju dolaska
# ## Za Francusku vidimo da je poslovno najveća 1435, te turisticka 2460
# ## Island ima samo turizam kao motivaciju te iznosi cijena 2500
# ## Italija za turizam 1700, poslovna 1190
# ## Njemačka turizam ima 2280, poslovna 1330
# ## Portugal samo turisticki ljudi putuju tamo i najveca cijena je 2475
# ## Španjolska turistički posjet karta je 2150, te poslovno je 1075
# ## Švedska samo turistički ljud dolaze i najveća cijena je 2760
# 

# In[71]:


prosjek_cijeneKarte=turisti_copy2["Price"].mean()


# In[72]:


prosjek_cijeneKarte


# In[73]:


turisti["Price average"]=(turisti_copy2["Price"]/prosjek_cijeneKarte)


# In[74]:


turisti.head(11)


# In[75]:


turisti["Price per day"]=(turisti_copy2["Price"]/turisti["NoDays"])


# In[76]:


turisti.head(11)


# ## Za feature/extraction uzeo sam prosjek cijene po karti i cijenu po danu

# In[ ]:




