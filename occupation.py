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




