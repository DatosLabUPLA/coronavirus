#!/usr/bin/env python
# coding: utf-8

# In[1]:

from django.db import models
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


url = 'https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/'


# In[3]:


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
}


# In[4]:


r = requests.get('https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/')
soup = BeautifulSoup(r.text,'html.parser')
tabla = soup.find('table')
df = pd.read_html(str(tabla),skiprows=1)[0]
df.index = df[0]
columns = list(df.iloc[0])
df.columns = columns
df = df.iloc[1:]
df = df[columns[1:]]
df