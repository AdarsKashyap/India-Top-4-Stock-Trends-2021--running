#!/usr/bin/env python
# coding: utf-8

# In[11]:


import yfinance as yf
import datetime
from datetime import date
import pandas as pd

stocks=["TCS.NS","INFY.NS","HDFC.NS","HUL.NS","RELIANCE.NS"]

Start_date= datetime.datetime.now()-datetime.timedelta(days=365*2)
today_date=date.today()

dataset=None
for indx,stock in enumerate(stocks):
    temp=yf.download(stock,start=Start_date,end=today_date)
    temp["Date"]=temp.index
    temp["Stock"]=stock
    if(indx==0):
        print("1")
        dataset=temp
    else:
        print("2")
        dataset=dataset.append(temp)


# In[ ]:




