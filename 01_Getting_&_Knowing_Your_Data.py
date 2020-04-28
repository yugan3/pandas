# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:57:38 2020

@author: Gan
"""

### Chipotle
### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset
path1 = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

### Step 3. Assign it to a variable called chipo
chipo = pd.read_csv(path1, sep = '\\t',engine = 'python')

### Step 4. See the first 10 entries
chipo.head(10)

### Step 5. What is the number of observations in the dataset?
chipo.info()
chipo.shape    #返回（行，列），tuple的形式

### Step 6. What is the number of columns in the dataset?
chipo.shape[1]    #DataFrame.shape() 返回（行，列），tuple的形式

### Step 7. Print the name of all the columns.
chipo.columns

### Step 8. How is the dataset indexed?
chipo.index

### Step 9. Which was the most-ordered item?
chipo[['item_name', 'quantity']].groupby('item_name').sum().sort_values(by='quantity')
# 因为分类下来只剩下quantity，因此对quantity进行聚合运算，运算结束进行排序

#Canned Soft Drink                           351
#Steak Burrito                               386
#Chips and Guacamole                         506
#Chicken Burrito                             591
#Chicken Bowl                                761

### Step 10. For the most-ordered item, how many items were ordered?
chipo[['item_name', 'order_id']].groupby('item_name').sum().sort_values(by = 'order_id',ascending = False)

### Step 11. What was the most ordered item in the choice_description column?
chipo[['choice_description','quantity']].groupby('choice_description').sum().sort_values('quantity',ascending = False).head(1)

### Step 12. How many items were orderd in total?
chipo['quantity'].sum()

### Step 13. Turn the item price into a float
chipo['item_price'].apply(lambda x: x.replace('$','')).astype('float')

#### Step 13.a. Check the item price type
chipo['item_price'].dtypes

#### Step 13.b. Create a lambda function and change the type of item price
w = chipo['item_price'].apply(lambda x : x.replace('$','')).astype('float')

#### Step 13.c. Check the item price type
w.dtypes

### Step 14. How much was the revenue for the period in the dataset?
q = (w*chipo['quantity']).sum() #要将字符串转化为数字才能计算

### Step 15. How many orders were made in the period?
c = chipo['order_id'].value_counts().count() #count是单纯计数

### Step 16. What is the average revenue amount per order?
chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
order_grouped.mean()['revenue']

### Step 17. How many different items are sold?"
chipo.item_name.value_counts().count() 
#不用去重的函数，因为value_counts确认数据出现的频率,已经分类汇总去重，直接计数即可






### occupation
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 22:18:12 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user)
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

### Step 3. Assign it to a variable called users and use the 'user_id' as index
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',
                      sep='|', index_col='user_id',engine ='python')

### Step 4. See the first 25 entries
users.head(25)

### Step 5. See the last 10 entries
users.tail(10)

### Step 6. What is the number of observations in the dataset?
users.shape[0]
users.info

### Step 7. What is the number of columns in the dataset?
users.shape[1]

### Step 8. Print the name of all the columns
users.columns

### Step 9. How is the dataset indexed?
users.index

### Step 10. What is the data type of each column?
users.dtypes

### Step 11. Print only the occupation column"
users['occupation']

### Step 12. How many different occupations there are in this dataset?
users['occupation'].value_counts().count()
users.occupation.nunique() #nuinque()这个函数分别统计每一列属性各自有多少个不同值

### Step 13. What is the most frequent occupation?
users['occupation'].value_counts().head(1, ascending = FALSE)

### Step 14. Summarize the DataFrame
users.describe()

### Step 15. Summarize all the columns
users.describe()

### Step 16. Summarize only the occupation column
users.occupation.describe()

### Step 17. What is the mean age of users?
users.age.mean()

### Step 18. What is the age with least occurrence?
users.age.value_counts().tail(1)




###World Food Facts
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 21:49:00 2020

@author: Gan
"""

import pandas as pd

### Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data

###  Step 2. Download the dataset to your computer and unzip it

### Step 3. Use the tsv file and assign it to a dataframe called food
food = pd.read_csv('https://www.kaggle.com/openfoodfacts/world-food-facts/data'
                   , engine = 'python', sep = '\\t')

### Step 4. See the first 5 entries
food.head(5)

### Step 5. What is the number of observations in the dataset?
food.shape()

### Step 6. What is the number of columns in the dataset?
food.shpae[1]
food.info()

### Step 8. What is the name of 105th column?
food.columns[104]

### Step 9. What is the type of the observations of the 105th column?
food.columns[104].dtypes

### Step 10. How is the dataset indexed?
food.index

### Step 11. What is the product name of the 19th observation?
food.values[18][7]   #直接用DataFrame.columns[][]查看即可，不用将数据提取出来

