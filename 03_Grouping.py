### alcohol

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:39:07 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv)
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'

### Step 3. Assign it to a variable called drinks.
drinks = pd.read_csv(url, engine = 'python')

### Step 4. Which continent drinks more beer on average?
drinks.groupby('continent').beer_servings.mean()
drinks.groupby('continent').beer_servings.sum()  
#针对分组下的某一特定值进行求和无非全员 DataFrame.groupby('A').B.聚合函数

### Step 5. For each continent print the statistics for wine consumption.
drinks.groupby('continent').wine_servings.describe()

### Step 6. Print the mean alcohol consumption per continent for every column
drinks.groupby('continent').mean()

### Step 7. Print the median alcoohol consumption per continent for every column
drinks.groupby('continent').median()

### Step 8. Print the mean, min and max values for spirit consumption.
#### This time output a DataFrame
drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])
#DataFrame.agg 是聚合函数的聚合函数，可以把不同的聚合函数放一起、




### occupation
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:15:03 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user)
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

### Step 3. Assign it to a variable called users.
users = pd.read_csv(url, sep = '|', engine = 'python')

### Step 4. Discover what is the mean age per occupation
users.groupby('occupation').age.mean()

### Step 5. Discover the Male ratio per occupation and sort it from the most to the least
#create a function to trasnfer the string to be data
def gender_numerical(x):
    if x == 'M':
        return  1
    if x == 'F':
        return  0

#apply the function for the data
a = users['gender_n'] = users['gender'].apply(gender_numerical) 
#直接在DataFrame中建立了一列
a.sort_values( ascending = False)

### Step 6. For each occupation, calculate the minimum and maximum ages
users.groupby('occupation').age.agg(['min', 'max'])

### Step 7. For each combination of occupation and gender, calculate the mean age
users.groupby(['occupation', 'gender']).age.mean()

### Step 8.  For each occupation present the percentage of women and men
# create a data frame and apply count to gender

gender_ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})
#先按照年龄和性别进行分组，然后根据分类中的某个标准进行统计，用的是键值对
#因为这里要统计的是性别下的人数，所以是对gender进行统计

# create a DataFrame and apply count for each occupation
occup_count = users.groupby(['occupation']).agg('count') #工作人员总数

# divide the gender_ocup per the occup_count and multiply per 100
occup_gender = gender_ocup.div(occup_count, level = 'occupation') * 100 #求比例
#DataFrame.div(a) DataFrame/a做除法

# present all rows from the 'gender column
occup_gender.loc[: , 'gender']



### regiment
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:46:15 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Create the DataFrame with the following values:
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
             'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
             'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
             'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
             'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

### Step 3. Assign it to a variable called regiment.
regiment = pd.DataFrame(raw_data, columns = ['regiment','company','name','preTestScore', 'postTestScore'])
regiment = pd.DataFrame(raw_data, columns = raw_data.keys()) 
#这里key的用法是因为键值对的原因，所以可以直接选择。这里有2中表示方法

### Step 4. What is the mean preTestScore from the regiment Nighthawks? 
regiment[regiment['regiment'] == 'Nighthawks'].groupby('regiment').mean() 
#当中是判断条件，相应的行数

### Step 5. Present general statistics by company
regiment.groupby('company').describe()

### Step 6. What is the mean each company's preTestScore?
regiment.groupby('company').preTestscore.mean() 
#分完组后仍然可以选择需要的维度进行聚合运算

### Step 7. Present the mean preTestScores grouped by regiment and company
regiment.groupby(['regiment', 'company']).preTestScore.mean()

### Step 8. Present the mean preTestScores grouped by regiment and company without heirarchical indexing
regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack() 
#without heirarchical 就是指把索引解压

### Step 9. Group the entire dataframe by regiment and company
regiment.set_index('company') # columns -> index
regiment.groupby(['regiment', 'company']).mean()

### Step 10. What is the number of observations in each regiment and company
regiment.groupby(['regiment','company']).size()

### Step 11. Iterate over a group and print the name and the whole data from the regiment
#iteration语句
for name, group in regiment.groupby('regiment'):
        # print the name of the regiment
    print(name) 
        # print the data of that regiment
    print(group)
    
