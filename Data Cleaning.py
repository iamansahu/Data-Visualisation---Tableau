#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df = pd.read_excel('Air Traffic Updated.xlsx')
df


# In[5]:


df.shape


# In[14]:


(df.isnull().sum()/len(df))*100


# # We found Operating Airline IATA Code and Published Airline IATA Code has some null values around 0.5% of the data in both.

# In[15]:


#remove null records

na_records = df[df.isna().any(axis=1)]


# In[16]:


na_records


# In[17]:


# make a seprate file for null records

na_records.to_csv('na_records.csv', index=False)


# In[20]:


new_df = df.dropna()


# In[22]:


# data without null

new_df.shape


# In[ ]:


# clean csv file

new_df.to_csv('new_df.csv', index=False)


# In[ ]:


LA_df = pd.read_excel('Book1.xlsx')
LA_df


# In[ ]:


LA_df.columns


# In[34]:


#drop unnecessary column

LA_df.drop(columns=['Unnamed: 6', 'Unnamed: 7','Unnamed: 8','Unnamed: 9'], inplace=True)


# In[37]:


#check any null values

LA_df.isna().sum()


# # there are no null values.

# In[ ]:


#export the clean data

LA_df.to_csv('LA_data.csv', index=False)


# In[ ]:




