### apple_stock
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:27:01 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'

### Step 3. Assign it to a variable apple
apple = pd.read_csv(url, engine = 'python')

### Step 4.  Check out the type of the columns
apple.info()

### Step 5. Transform the Date column as a datetime type
apple['Date'] = pd.to_datetime(apple.Date)
# pd.to_datetime 是转换时间格式

### Step 6.  Set the date as the index
apple = apple.set_index('Date')

### Step 7.  Is there any duplicate dates?
apple.index.is_unique 
# 判断是不是有重复值

### Step 8.  Ops...it seems the index is from the most recent date. Make the 
### first entry the oldest date.
apple = apple.sort_index(ascending = True)
# index的排序有sort_index可以直接使用，而DataFrame中的value排序要sort_values(by=)
# columns直接重新选择就可以排序了

### Step 9. Get the last business day of each month
apple_month = apple.resample('BM').mean()
# 重新抽样取值， BM是月底的频率

### Step 10.  What is the difference in days between the first day and the oldest
(apple.index.max() - apple.index.min()).days
# date是index分别找max和min，然后转化为天数

### Step 11.  How many months in the data we have?
apple_months = apple.resample('BM').mean()
len(apple_months)

### Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9
### inches
appl_open = apple['Adj Close'].plot(title = 'Apple Stock')
# 直接画图，而不是选择图形
fig.set_size_inches(13.5, 9)







### financial_data
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:06:25 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import datetime as dt

### Step 2. Create your time range (start and end variables). The start date 
### should be 01/01/2015 and the end should today (whatever your today is)
start = dt.datetime(2015,1,1)
end = dt.datetime.today()
# dt.datetime(year,month,day)

### Step 3. Select the Apple, Tesla, Twitter, IBM, LinkedIn stocks symbols and 
### assign them to a variable called stocks
stocks = ['Apple', 'Tesla', 'Twitter', 'IBM']

### Step 4. Read the data from google, assign to df and print it
df = web.DataReader(stocks, 'google', start, end)

### Step 5.  What is the type of structure of df ?
df.info()

### Step 6. Print all the Items axis values
#### To learn more about the Panel structure go to [documentation](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#panel)
df.items
# items 是返回key:value的键值对

### Step 7. Good, now we know  the data avaiable. Create a dataFrame called 
### vol, with the Volume values
vol = df['Volume']

### Step 8. Aggregate the data of Volume to weekly
#### Hint: Be careful to not sum data from the same week of 2015 and other years

# 不同年中的相同月份，就需要用year和week两个指标来区分
vol['week'] = vol.index.week
vol['year'] = vol.index.year
# DataFrame.index.week/year 是pandas中处理时间序列的命令，针对的是标准时间格式
week = vol.groupby(['week','year']).sum()

### Step 9. Find all the volume traded in the year of 2015
del vol['week']
vol['year'] = vol.index.year 
# 重新按照年份来标志
trade = vol.groupby('year').sum()






### investor
### apple_stock
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:39:24 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv).
url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'

### Step 3. Assign it to a variable called df
df = pd.read_csv(url, engine ='python')

### Step 4.  What is the frequency of the dataset?"

### Step 5. Set the column Date as the index.
df = df.set_index('Date')

### Step 6. What is the type of the index
df.index.dtype()

### Step 7. Set the index to a DatetimeIndex type
df.index = df.to_datetime(df.index)
# pd.to_datetime 和 dt.datetime(year,month,day)的效果是一样的

### Step 8. Change the frequency to monthly, sum the values and assign it to monthly.
monthly = df.resample('M').sum()

### Step 9. You will notice that it filled the dataFrame with months that don't
### have any data with NaN. Let's drop these rows.
monthlt = monthly.dropna()

### Step 10. Good, now we have the monthly data. Now change the frequency to year.
yearly = df.resample('Y').sum()
year = monthly.resample('AS-JAN').sum()
# AS是年初的频率




