# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:34:26 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'

### Step 3. Assign it to a variable called euro12
euro12 = pd.read_csv(url, sep ='\\t', engine = 'python')

### Step 4. Select only the Goal column.
euro12.Goals

### Step 5. How many team participated in the Euro2012?
euro12.shape[0]

### Step 6. What is the number of columns in the dataset?
euro12.shape[1]
euro12.info()

### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team','Yellow_Cards','Red_Cards']]

### Step 8. Sort the teams by Red Cards, then to Yellow Cards
discipline.sort_values( by = ['Red_Cards', 'Yellow_Cards'], ascending =False)

### Step 9. Calculate the mean Yellow Cards given per Team
discipline['Yellow_Cards'].mean()

### Step 10. Filter teams that scored more than 6 goals
euro12[euro12.Goals>6]

### Step 11. Select the teams that start with G
euro12[euro12.Team.str.startwith('G')]
#DataFrame.str.startwith() 以xx开头的字符串
#DataFrame.str.endwith() 以xx结尾的字符串
#DataFrame.str.contain() 包含xx的字符串

### Step 12. Select the first 7 columns
euro12.iloc[:,0:7] #iloc不包含端点

### Step 13. Select all columns except the last 3
euro12.iloc[:,:-3] #倒数从-1到-3

### Step 14. Present only the Shooting Accuracy from England, Italy and Russia
euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]