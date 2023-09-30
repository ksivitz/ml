#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import requests
import requests as r
from pandas.io.json import json_normalize
import json
from bs4 import BeautifulSoup
from datetime import date


# In[19]:


holidays = ['2023-11-23', '2023-12-25','2024-01-01','2024-01-15','2024-02-19','2024-03-29','2024-05-27','2024-06-19','2024-07-04','2024-09-02','2024-11-28','2024-12-25']


# In[22]:


today = date.today()


# In[24]:


weekday = today.weekday()


# In[ ]:


'''
if str(today) in holidays:
    return
if weekday = 5:
    return
if weekday = 6:
    return
'''


# In[2]:


pip install fear-and-greed


# In[3]:


df = pd.read_csv('https://raw.githubusercontent.com/ksivitz/ml/main/new_data.csv')


# In[4]:


df.tail()


# In[5]:


for i in range(len(df.columns)):
    print(df.columns[i])


# In[6]:


def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row       
    return rows


# In[7]:


new_row = []


# In[8]:


today = date.today()


# In[9]:


new_row.append(str(today))


# In[10]:


URL = "https://www.cnbc.com/quotes/SPY"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

today_open = float(soup.find('span', class_='SplitStats-price').text)

close_ish = float(soup.find('span', class_='QuoteStrip-lastPrice').text)

volume = float(soup.find('div', class_='QuoteStrip-volume').text.replace(',',''))

new_row.append(volume)


# In[11]:


dow = today.weekday()
new_row.append(dow)


# In[12]:


month = today.month
new_row.append(month)


# In[13]:


dom = today.day
new_row.append(dom)


# In[14]:


p_diff = (today_open-close_ish)/close_ish
new_row.append(p_diff)


# In[15]:


# 10-year
URL = "https://www.cnbc.com/quotes/US10Y"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

rate = soup.find_all('span', class_="QuoteStrip-lastPrice")
rate = float(rate[0].text[:-1])
new_row.append(rate)


# In[16]:


#hike / cut probability

URL = "https://www.investing.com/central-banks/fed-rate-monitor"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
tables = soup.find_all('div', class_="percfedRateItem")
for i in [0,1]:
    if 'Blue' in str(tables[i].find_all('div')[0]):
        current = float(tables[i].find_all('span')[0].text[:4])
    if 'Grey' in str(tables[i].find_all('div')[0]):
        new = float(tables[i].find_all('span')[0].text[:4])
        percent = float(tables[1].find_all('span')[1].text[:-1])
if current < new:
    hike = percent
    cut=0
else:
    hike=0
cut=percent

new_row.append(hike)
new_row.append(cut)


# In[17]:


#US Dollar Index

URL = "https://www.marketwatch.com/investing/index/dxy?mod=search_symbol"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
data = json.loads(soup.find('script', type='application/ld+json').text)
price = float(data['price'])

new_row.append(price)


# In[18]:


#Oil price and change

URL = "https://www.eia.gov/petroleum/weekly/crude.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

tables = soup.find_all('table', class_ ='basic-table full-width highlight-col-2')

data = tableDataText(tables[1])  
barrels = float(data[2][1])
barrel_change = float(data[2][1])-float(data[2][2])

new_row.append(barrels)
new_row.append(barrel_change)


# In[26]:


#CPI
URL = "https://www.investing.com/economic-calendar/cpi-733"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
cp = soup.find('div', class_="arial_14 greenFont").text
cpi = float(cp[:-1])

new_row.append(cpi)


# In[19]:


#Jobless claims (3)
URL = "https://fred.stlouisfed.org/release/tables?rid=180&eid=258888#snid=258889"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
tables = soup.find_all('div', class_="table-responsive")
data = tableDataText(tables[0])  

init = data[1][2][:-6]
init = float(init.replace(',',''))

cont = data[4][2][:-6]
cont = float(cont.replace(',',''))

four_week = data[3][2][:-6]
four_week = float(four_week.replace(',',''))

new_row.append(init)
new_row.append(cont)
new_row.append(four_week)


# In[20]:


#CNN

import fear_and_greed

f_g = fear_and_greed.get().value
new_row.append(f_g)


# In[21]:


#CNN_dif
cnn_dif = f_g - df['CNN'].values[-1]
new_row.append(cnn_dif)


# In[22]:


#lags
def make_lags(ts, lags): # creates dataframe of lag features for time series data
    return pd.concat(
        {
            f'y_lag_{i}': ts.shift(i)
        for i in range(1, lags + 1)
        },
        axis=1)


# In[23]:


close_lags = make_lags(df['tom_resid'], lags=6)

for i in range(len(close_lags.iloc[-1].values)):
    new_row.append(close_lags.iloc[-1].values[i])


# not used

# In[24]:


#oil futures
URL = "https://www.marketwatch.com/investing/future/cl.1"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
data = json.loads(soup.find('script', type='application/ld+json').text)
price = float(data['price'])

#new_row.append(price)


# In[25]:


#put call ratio open interest
URL = "https://www.alphaquery.com/stock/SPY/volatility-option-statistics/30-day/put-call-ratio-oi"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data = soup.find_all('div', class_= "indicator-figure-inner")
oi_rate = float(data[8].text)

#new_row.append(oi_rate)


# In[26]:


#open interest volume

URL = "https://www.alphaquery.com/stock/SPY/volatility-option-statistics/30-day/put-call-ratio-oi"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data = soup.find_all('div', class_= "indicator-figure-inner")
oi_volume = float(data[7].text)

#new_row.append(oi_volume)


# In[27]:


# IV ratio 
URL = "https://www.alphaquery.com/stock/SPY/volatility-option-statistics/30-day/put-call-ratio-oi"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data = soup.find_all('div', class_= "indicator-figure-inner")
oi_ratio = float(data[5].text)

#new_row.append(oi_ratio)


# end not used

# In[28]:


new_row


# In[29]:


len(new_row)


# In[30]:


new_row.append(0)


# In[31]:


df.loc[len(df)] = new_row


# In[32]:


df.head(10)


# In[33]:


from statsmodels.tsa.deterministic import DeterministicProcess
from statsmodels.tsa.deterministic import CalendarFourier
from statsmodels.tsa.stattools import pacf

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


# In[34]:


def lin_predictions():

        df_close = pd.read_csv('https://raw.githubusercontent.com/ksivitz/ml/main/close_test.csv')
        df_close = df_close.set_index('Date')
        df_close.index = df_close.index.astype(str)
        df_close.index = pd.to_datetime(df_close.index)
        df_close.index = df_close.index.to_period('D')

        df_close = df_close[~df_close.index.duplicated(keep='last')]
        
        arry = df_close['Close'][:]# creates Series of sales data 
        fourier = CalendarFourier(freq="A", order=12) # creates calander fourier values

        # defines dataframe consisting of constant and trend values of timeseries, with date as the index 
        dp = DeterministicProcess(
        index=df_close.index,
        constant=True,               
        order=2,                     
        seasonal=True,               
        additional_terms=[fourier],  
        drop=True,
        )

        X = dp.in_sample() # creates deterministic dataframe for dates in index

        X2 = make_lags(arry, lags=3) # creates lag features for sales values
        X2 = X2.fillna(0.0) # fills null values with 0.0

        X3 = pd.merge(X,X2, left_on = X.index, right_on = X2.index) # combine dp and lag dataframes
        X3 = X3.set_index('key_0') # sets id as index

        y = arry[:] # creates copy of sales values by date (y)

        X_train, X_test, y_train, y_test = train_test_split(X3, y, test_size=1, shuffle=False) # splits data into train, test datasets
        
        # Fit and predict
        global lin_model
        lin_model = LinearRegression() # defines linear regression model
        lin_model.fit(X_train, y_train) # fits model to training data.
        
        return X_test


# In[35]:


X_test = lin_predictions()
pred = lin_model.predict(X_test)


# In[36]:


resid = close_ish - pred[0]


# In[37]:


df.iloc[-3, df.columns.get_loc('tom_resid')] = resid


# In[38]:


df.tail()


# In[41]:


closing = pd.read_csv("https://raw.githubusercontent.com/ksivitz/ml/main/close_test.csv")


# In[43]:


closing.loc[len(closing)] = [today, close_ish]


# In[44]:


closing.tail()


# In[48]:


closing.to_csv('new_close.csv')


# In[49]:


df.to_csv('new_data.csv')


# In[ ]:





# In[ ]:





# In[ ]:




