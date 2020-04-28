### army

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:54:12 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. This is the data given as a dictionary
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
             'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
             'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
             'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
             'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
             'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
             'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
             'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
             'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

### Step 3. Create a dataframe and assign it to a variable called army.
army = pd.DataFrame(raw_data, columns = ['regiment','company','deaths','battles','size','veterans','readiness','armored','deserters',  'origin'])

### Step 4. Set the 'origin' colum as the index of the dataframe
army = army.set_index('origin')

### Step 5. Print only the column veterans
army['veterans']

### Step 6. Print the columns 'veterans' and 'deaths'
army[['veterans', 'deaths']]

### Step 7. Print the name of all the columns.
army.columns

### Step 8. Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska
army.loc[army.origin.isin('Maine', 'Alaska'), ['deaths', 'size', 'deserters']]
army.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']] #都是索引所以用loc，另外origin已经变成index所以可以直接使用

### Step 9. Select the rows 3 to 7 and the columns 3 to 6
army.iloc[3:7, 3:6]  # iloc是左闭右开，即[,)

### Step 10. Select every row after the fourth row
army.iloc[3:]

### Step 11. Select every row up to the 4th row
army.iloc[:3]

### Step 12. Select the 3rd column up to the 7th column
army.iloc[:,4:7]

### Step 13. Select rows where df.deaths is greater than 50
army[army['deaths']>50]

### Step 14. Select rows where df.deaths is greater than 500 or less than 50
army[(army['deaths']>500) | (army['deaths']<50)] #不要用文字的and 和 or

### Step 15. Select all the regiments not named \"Dragoons\"
army[army['regiments' != 'Dragoons']]

### Step 16. Select the rows called Texas and Arizona
army.loc[['Texas','Arizona']]

### Step 17. Select the third cell in the row named Arizona
army.loc['Arizona','deaths']

### Step 18. Select the third cell down in the column named deaths
army.loc['Texas', 'deaths']





### chipotle
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






### euro
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