### iris
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:55:13 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

### Step 3. Assign it to a variable called iris
iris = pd.read_csv(url, engine ='python')

### Step 4. Create columns for the dataset
iris.columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class']

### Step 5.  Is there any missing value in the dataframe?
iris.isnull()
iris.iloc[10:30,2:3] = np.nan

### Step 7. Good, now lets substitute the NaN values to 1.0
iris = iris.petal_length.fillna(1, inplace = True)
# inplace表示在源数据上进行填充和修改

### Step 8. Now let's delete the column class
del iris['class']

### Step 9.  Set the first 3 rows as NaN
iris.iloc[0:3,:] = np.NaN

### Step 10.  Delete the rows that have NaN
iris = iris.dropna(how='any', inplace = True)
# inplace表示在源数据上进行填充和修改

### Step 11. Reset the index so it begins with 0 again
iris = iris.reset_index(drop = True)
# drop表示不保留原来的index， 默认为False





### wine
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:35:52 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'

### Step 3. Assign it to a variable called wine
wine = pd.read_csv(url, engine = 'python')

### Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns
wine = wine.drop(wine.columns[[0,3,6,8,11,12,13]], axis = 1)
# 删掉的命令DataFrame.drop = del， 后面DataFrame.columns([])可以直接用列的数字
# 表示索引，不一定要列名; axis = 1表示columns，0表示row(index), 删除row直接带上
# index，以及axis = 0 即可

### Step 5. Assign the columns as below:
### 1) alcohol
### 2) malic_acid
### 3) alcalinity_of_ash
### 4) magnesium
### 5) flavanoids
### 6) proanthocyanins
### 7) hue
wine.columns = ['alchol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 
                'flavanoids', 'proanthocyanins', 'hue']

### Step 6. Set the values of the first 3 rows from alcohol as NaN
wine.alchol.iloc[0:3] = np.NaN

### Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN
wine.iloc[2:4, 3] = np.nan

### Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
wine.alchol.fillna(10, inplace = True)
wine.magnesium.fillna(100, inplace = True)

### Step 9. Count the number of missing values
wine.isnull().sum()

### Step 10.  Create an array of 10 random numbers up until 10
array = np.random.randint(10, size =10)

### Step 11. Use random numbers you generated as an index and assign NaN value
### to each of cell.
# 题目的意思是随机在列中增加nan
wine.alchol[np.random.randint(20,size =19)] = np.nan

### Step 12.  How many missing values do we have?
wine.isnull().sum()

### Step 13. Delete the rows that contain missing values
wine = wine.dropna(axis = 0, how = 'any')
# 一定要标注清楚维度，axis = 0 是row，而 axis = 1 是column

### Step 14. Print only the non-null values in alcohol
print(wine.alchol[wine.alchol.isnull() == False])
# DataFrame.notnull()有现成的命令
mask = wine.alchol.notnull()
wine.alchol[mask]

### Step 15.  Reset the index, so it starts with 0 again
wine = wine.reset_index(drop = True)




