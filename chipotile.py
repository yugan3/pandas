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