### crime

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:56:07 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'

### Step 3. Assign it to a variable called crime.
crime = pd.read_csv(url, engine ='python')

### Step 4. What is the type of the columns?
crime.info()

### Step 5. Convert the type of the column Year to datetime64
x = pd.to_datetime(crime.Year, format='%Y')
# pd.to_datetime(a, format='%Y-%m-%d-%H-%M-%S')
x.info()

### Step 6. Set the Year column as the index of the dataframe
crime.set_index('Year'， drop = True) # drop为保留原来的数据

### Step 7. Delete the Total column
crime.drop(['Total', axis = 1 ])
# axis = 1表示列， axis = 0 表示行
del crime['Total']  #使用内置函数del

### Step 8. Group the year by decades and sum the values
#### Pay attention to the Population column number, summing this column is a mistake
# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()   #重新抽样
# resample：在给定的时间单位内重取样
# groupby：对给定的数据条目进行统计
# DataFrame.resample(rule)，这里的rule包括：
# A year
# M month
# W week
# D day
# H hour
# T minute
# S second
# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10S').max() #取最大值
# Updating the "Population" column
crimes['Population'] = population

### Step 9. What is the mos dangerous decade to live in the US?
crime.idxmax(0)
#DataFrame.idxmax() 根据每一列，索引搜索最大值



# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:22:09 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'

### Step 3. Assign it to a variable called df
df = pd.read_csv(url, engine = 'python') # csv逗号分隔符不用指定sep，默认即可

### Step 4. For the purpose of this exercise slice the dataframe from 'school' 
### until the 'guardian' column
df_slice = df.loc[:,'school':'guardian']
df_slice.head(10)

### Step 5. Create a lambda function that capitalize strings.
capitalizer = lambda x: x.capitalize()

### Step 6. Capitalize both Mjob and Fjob
df_slice['Mjob'].apply(capitalizer)
df_slice['Fjob'].apply(capitalizer)

### Step 7. Print the last elements of the data set.
df.tail(1)

### Step 8. Did you notice the original dataframe is still lowercase? 
### Why is that? Fix it and capitalize Mjob and Fjob.
# 改变DataFrame，如果是添加，则直接输入新的列的名称即可
# 改变DataFrame，如果是替换，则直接将原有的列对应等于新的即可
# DataFrame没有直接的capitalize的功能，所以只能筛选出对应数据进行替换，也就是不能
# 直接把数字放到Capitalize中进行操作
df['Mjob'] = df_slice['Mjob'].apply(capitalizer)
df['Fjob'] = df_slice['Fjob'].apply(capitalizer)

### Step 9. Create a function called majority that return a boolean value to a 
### new column called legal_drinker (Consider majority as older than 17 years old)
# 分成两部分：先写函数生成布尔逻辑值，再把逻辑值放到DataFrame中。不是直接把结果返回

def majority(x):
    if x >17:
        return True
    if x <= 17:
        return False
    
df['legal_drinker'] = df['age'].apply(majority)

### Step 10. Multiply every number of the dataset by 10. \n",
##### I know this makes no sense, don't forget it is just an exercise" 
# 不是直接数字乘以10，而是将数字乘以10。如果直接把string乘以10，只是把数字复制10遍
def times10(x):
    if type(x) is int: # 使用内置函数，而不是pandas的性质
        return x*10
    
