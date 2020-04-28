### baby_name
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:05:43 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'

### Step 3. Assign it to a variable called baby_names.
baby_names = pd.read_csv(url, engine ='python')

### Step 4. See the first 10 entries
baby_names.head(10)

### Step 5. Delete the column 'Unnamed: 0' and 'Id
del baby_names['Unnamed: 0']
del baby_names['Id']

### Step 6. Are there more male or female names in the dataset?
baby_names['Gender'].value_counts()

### Step 7. Group the dataset by name and assign to names
del baby_names['year']
names = baby_names.groupby('name').sum()
names.sort_value('Count', ascending = False)

### Step 8. How many different names exist in the dataset?
len(names) #因为已经分组，所以去重完成

### Step 9. What is the name with most occurrences?
names.sort_value('Count', ascending = False).head(1)
names.Count.idxmax() #count是计数

### Step 10. How many different names have the least occurrences?
len(names[names.Count == names.Count.min()]) # A.min求最小值，A.max求最大值

### Step 11. What is the median name occurrence?
names[names.Count ==names.Count.median()]

### Step 12. What is the standard deviation of names?
names.Count.std()

### Step 13. Get a summary with the mean, min, max, std and quartiles.
names.describe()




### wind_status
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:34:51 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

### Step 2. Import the dataset from this [address](https://github.com/guipsamora/pandas_exercises/blob/master/06_Stats/Wind_Stats/wind.data)
url = 'https://github.com/guipsamora/pandas_exercises/blob/master/06_Stats/Wind_Stats/wind.data'

### Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.
data = pd.read_csv(url, sep = 's+', parse_dates = [[0,1,2]], engine = 'python' )
# 指定parse_dates = [ ['time', 'date'] ]，即将[ ['time', 'date'] ]两列的字符串先
# 合并后解析方可。合并后的新列会以下划线'_'连接原列名命名, 格式会自动按照正确的显示

### Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.
# The problem is that the dates are 2061 and so on...
def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
# apply the function fix_century on the column and replace the values to the right ones\n",
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

### Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])
# pd.to_datetime('13000101', format='%Y%m%d', errors='ignore') 非标准时间样式
# datetime.datetime(1300, 1, 1, 0, 0)
# data= pd.to_datetime(data) #标准时间格式，只是格式，变成日期类型

### Step 6. Compute how many values are missing for each location over the entire record.
#### They should be ignored in all calculations below. 
data.isnull().sum() # 将列中为空的个数统计出来
# 判断缺失值一般采用 isnull()，生成的是所有数据的true/false矩阵，常用的语法是
# df[df.isnull().values==True] 只显示缺失值的位置

### Step 7. Compute how many non-missing values there are in total.
data.count() # count只统计非缺失值
data.shape[0] - data.isnull().sum()
data.notnull().sum() # 对应前面的isnull

### Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
#### A single number for the entire dataset.
data.fillna(0).values.flatten().mean()
# DataFrame.values 将表中的数字变成数值（比如原来是字符串格式）
# data.fillna(0)使用0将缺失值填充，便于后面均值计算
# flatten是把所有的分组合并都一个array中，所以就只有一个对应的mean了

### Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days 
#### A different set of numbers for each location.
loc_stats = data.describe(percentiles=[]) # 不需要分位点

### Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
#### A different set of numbers for each day.

# create the dataframe
day_stats = pd.DataFrame
day_stats['Yr_Mo_Dy'] = data['Yr_Mo_Dy']
# this time we determine axis equals to one so it gets each row.
day_stats['min'] = data.min(axis = 1) 
day_stats['max'] = data.max(axis = 1)
day_stats['mean'] = data.mean(axis = 1)
day_stats['std'] = data.std(axis = 1)

### Step 11. Find the average windspeed in January for each location. 
#### Treat January 1961 and January 1962 both as January."
data[data['Mo' == 1]].mean() # 选取的是行
data.loc[data.index.month == 1].mean()

### Step 12. Downsample the record to a yearly frequency for each location.
data.groupby(data.index.to_period('A')).mean()
# to_period 按照月（'M'）或年（'A'）的方式现实，但不统计，只是有一个计数
# 原来的索引是datatime，时间格式

### Step 13. Downsample the record to a monthly frequency for each location.
data.groupby(data.index.to_periods('M')).mean()

### Step 14. Downsample the record to a weekly frequency for each location.
data.groupby(data.index.to_period('W')).mean()
            
### Step 15. Calculate the min, max and mean windspeeds and standard deviations 
# of the windspeeds across all locations for each week (assume that the first 
# week starts on January 2 1961) for the first 52 weeks.

weekly = data.resample('W').agg(['min','max','mean','std']
weekly.loc[weekly.index[1:53], 'RPT':'MAL']
# resample data to 'W' week and use the functions
# slice it for the first 52 weeks and locations
# 这里的切片就是表示重新按照星期取样的数据是从1月2日开始的，所以从左端取1
# resample是针对时间频率转化和时间序列重新采样的一个常见方式