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

