# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:06:50 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv)
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep = '\\t', engine = 'python')

### Step 3. Assign it to a variable called chipo
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep = '\\t', engine = 'python')

### Step 4. How many products cost more than $10.00(quantity=1)?
price = chipo['item_price'].apply(lambda a: a.replace('$', ' ')).astype('float')
price.dtpyes
chipo.item_price = price
q = chipo[['item_name','item_price']][chipo.item_price >10]
q.nunique()[0]
# DataFrame.drop_duplicates(subset=['A','B'],keep='first/last/False'（保留第一次/
# 最后一次/全部删除）,inplace=True（是否生成新副本，默认False即生成）)
# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])
# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1],
chipo_one_prod[chipo_one_prod['item_price']>10].item_name.nunique()

### Step 5. What is the price of each item? 
###### print a data frame with only two columns item_name and item_price
chipo_filtered = chipo.drop_duplicates['item_name','quantity']
chipo_one_prod = chipo_filtered[chipo_filtered['quantity'] == 1 ] 
#单价，所以选择quantity为1
price_per_item = chipo_one_prod[['item_name', 'item_price']] #only two columns
price_per_item.sort_values(by = 'item_price', ascending = 'False').head(20)

### Step 6. Sort by the name of the item
chipo.sort_values(by = 'item_name')

### Step 7. What was the quantity of the most expensive item ordered?
chipo.sort_values(by = 'item_price', asecnding = 'False').quantity.head(1)

### Step 8. How many times were a Veggie Salad Bowl ordered?
chipo[chipo.item_name == 'Veggie Salad Bowl'].count()
chipo[chipo.item_name == 'Veggie Salad Bowl'].len() #len()统计出现的行数

### Step 9. How many times people orderd more than one Canned Soda?
chipo_soda = chipo[(chipo.item_name == 'Canned Soda') & (chipo.quantity > 1)]
# 可以将两个条件同时并列放在括号中，用&连接
chipo_soda.len()
# 区分
# len 查看该列的行数
# count 查看该列值的有效个数，不包含无效值（Nan）