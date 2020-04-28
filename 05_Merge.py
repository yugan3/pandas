### housing market

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:23:50 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

### Step 2. Create 3 differents Series, each of length 100, as follows: 
# 1. The first a random number from 1 to 4
# 2. The second a random number from 1 to 3
# 3. The third a random number from 10,000 to 30,000

first = pd.Series(np.random.randint(1,4,100, dtype = 'l'))
second = pd.Series(np.random.randint(1,3,100, dtype = 'l'))
third = pd.Series(np.random.randint(10000,30000,100, dtype = 'l'))
#这里pd.Series是为了能够有标记index，所以进行类型转换，否则就是array的格式

### Step 3. Let's create a DataFrame by joinning the Series by column
df = pd.concat([first, second, third], axis = 1) # 直接合并数据，不是字符串，所以不需要引号

### Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter
df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']
df.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True) 
# 用rename的函数重新命名

### Step 5. Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'
# 在dataframe中将三列变成一列
df_col = pd.concat([first, second, third], axis =0 )
big_column = df_col.to_frame() # 将Series转化为DatasFrame

### Step 6. Ops it seems it is going only until index 99. Is it true?
len(big_column)

### Step 7. Reindex the DataFrame so it goes from 0 to 299
big_column.reset_index(drop=True, inplace=False,) #这里的drop表示删除原来的索引




### MPG_cars
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:30:16 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the first dataset [cars1](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv)and[cars2](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv)
url1 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv'
url2 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv'

### Step 3. Assign each to a to a variable called cars1 and cars2
cars1 = pd.read_csv(url1, engine = 'python')
cars2 = pd.read_csv(url2, engine = 'python')

### Step 4. Ops it seems our first dataset has some unnamed blank columns, fix cars1
# 把有效值取出来就好了，不同dropna
cars1 = cars1.loc[:,'mpg':'car']

### Step 5. What is the number of observations in each dataset?
cars1.shape
cars2.shape

### Step 6. Join cars1 and cars2 into a single DataFrame called cars
cars = cars1.append(cars2)
# append是将元素添加到后面，即在DataFrame中是添加到行的后面

### Step 7. Ops there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.
import numpy as np
owner= np.random.randint(15000,73000,398)

### Step 8. Add the column owners to cars
cars['owner'] = owner






### names
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:51:23 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Create the 3 DataFrames based on the followin raw data
raw_data_1 = {
        'subject_id':['1','2','3','4','5'],
        'first_name':['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
        
### Step 3. Assign each to a variable called data1, data2, data3
data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])

### Step 4. Join the two dataframes along rows and assign all_data
all_data = pd.concat([data1,data2]) # axis = 0,按照行rows添加
#将所有的相应列都添加到一起，却是的部分会用NaN表示，例如：pd.concat([data1,data3])

### Step 5. Join the two dataframes along columns and assing to all_data_col
# 将对应列添加在一起，比如A表中对应B表只的列
all_data_col = pd.concat([data1, data2], axis = 1) # axis = 1， 按照columns来添加

### Step 6. Print data3
print(data3)

### Step 7. Merge all_data and data3 along the subject_id value
data_merge = pd.merge(all_data, data3, on = 'subject_id')

### Step 8. Merge only the data that has the same 'subject_id' on both data1 and data2
data_merge_12 = pd.merge(data1,data2, on = 'subject_id', how ='inner')

