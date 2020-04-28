### Chipotle_visualization
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:28:20 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv)
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

### Step 3. Assign it to a variable called chipo.
chipo = pd.read_csv(url, sep = '\\t', engine = 'python')

### Step 4. See the first 10 entries
chipo.head(10)

### Step 5. Create a histogram of the top 5 items bought
top5item = chipo.groupby('item_name').sum().sort_values(by = 'quantity', ascending = False).head(5)
import matplotlib.pyplot as plt
import collections
del top5item['order_id']
top5item.plot(kind='bar') # bar是直方图，plot法一：直接在DataFrame后面加plot属性
plt.xlabel('Items')
plt.ylabel('Price')
plt.title('Most ordered Chipotle\'s Items')
plt.show()

### Step 6. Create a scatterplot with the number of items orderered per order price
#### Hint: Price should be in the X-axis and Items ordered in the Y-axis
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price]
chipo.item_price = chipo['item_price'].apply(lambda x: x.replace('$', '').asypte('float'))
orders = chipo.groupby('order_id').sum()
plt.scatter(orders.quantity, orders.item_price, s = 50, c = 'green') 
# scatter是散点图，法二：plt.scatter，利用plot的属性来画图，然后将需要的数据引用
plt.xlabel('quantity')
plt.ylabel('item_price')
plt.title('number of ordered per order price')
plt.ylim(0) # plt.ylim()和plt.xlim()表示坐标轴的起点，同样也可以设置最大值的范围
plt.show()





### online_retail
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:34:30 2020

@author: Gan
"""

### Step 1. Import the necessary libraries"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(style= 'ticks')

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv'

### Step 3. Assign it to a variable called online_rt
### Note: if you receive a utf-8 decode error, set `encoding = 'latin1' in pd.read_csv()
online_rt = pd.read_csv(url, engine = 'python', encoding = 'latin1')
online_rt.head(10)

### Step 4. Create a histogram with the 10 countries that have the most 
### 'Quantity' ordered except UK
country = online_rt[online_rt['country'] != 'UK'].groupby('country').sum().sort
_values(by = 'quantity', ascending = False).head(10)
country = country[['country', 'quantity']]
country.plot(kind = 'bar')
plt.xlabel('country')
plt.ylabel('quantity')
plt.title('top 10 countries with most quantity')
plt.show()

countries = online_rt.groupby('Country').sum()
countries = countries.sort_values(by = 'Quantity',ascending = False)[1:11]
# sort the value and get the first 10 after UK
countries['Quantity'].plot(kind='bar')
plt.xlabel('Countries')
plt.ylabel('Quantity')
plt.title('10 Countries with most orders')
plt.show()


### Step 5.  Exclude negative Quatity entries
online_rt = online_rt[online_rt.quantity > 0 ]

### Step 6. Create a scatterplot with the Quantity per UnitPrice by CustomerID 
### for the top 3 Countries
customers = online_rt.groupby(['country', 'unitprice']).sum()
customers = customers[customers.quantity > 0 ]

# get the value of the index and put in the column Country
customers['Country'] = customers.index.get_level_values(1)
# DataFrame.index.get_level_values()是获取对应级别的索引

# top three countries
top_countries =  ['Netherlands', 'EIRE', 'Germany']
# filter the dataframe to just select ones in the top_countries
customers = customers[customers['Country'].isin(top_countries)]

############# graph section #############
g = sns.FacetGrid(customers, col='Country') 
# 简历网格图 sns.FacetGrid(DataFrame, col, index)
g.map(plt.scatter, 'Quantity', 'UnitPrice', alpha=1)
# 创建网格图上的图形
g.add_legend()
# 绘制一个图例，可能将其放在轴外并调整图形大小

### Step 7. Investigate why the previous results look so uninformative
#### Step 7.1 Look at the first line of code in Step 6. And try to figure out 
### if it leads to any kind of problem
##### Step 7.1.1 Display the first few rows of that DataFrame

### This takes our initial dataframe groups it primarily by 'CustomerID' and 
### secondarily by 'Country'
# It sums all the (non-indexical) columns that have numerical values under 
### each group
customers = online_rt.groupby(['CustomerID','Country']).sum().head()

##### Step 7.1.2 Think about what that piece of code does and display the dtype 
### of UnitPrice
online_rt['UnitPrice'].dtype()
#So it's 'float64'
#If 'UnitPrice' wasn't something that we were interested in then it would be OK
# since we wouldn't care whether UnitPrice was being summed or not
# But we want our graphs to reflect 'UnitPrice'!
# Note that summing up 'UnitPrice' can be highly misleading.
# It doesn't tell us much as to what the customer is doing.






### scores
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:18:13 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import matpoltlib.pyplot as plt
 "  first_name last_name  age  female  preTestScore  postTestScore\n",
       "0      Jason    Miller   42       0             4             25\n",
       "1      Molly  Jacobson   52       1            24             94\n",
       "2       Tina       Ali   36       1            31             57\n",
       "3       Jake    Milner   24       0             2             62\n",
       "4        Amy     Cooze   73       1             3             70"
### Step 2. Create the DataFrame it should look like below
raw_data = {
        'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'female' : [0, 1, 1, 0, 1],
        'preTestScore' : [4, 24, 31, 2, 3],
        'postTestScore' : [25, 94, 57, 62,70]}

df = pd.DataFrame (raw_data, columns = ['first_name', 'last_name', 'age', 
                  'female', 'preTestscore', 'postTestscore'])

### Step 3. Create a Scatterplot of preTestScore and postTestScore, with the 
### size of each point determined by age
plt.scatter(df.preTestscore, df.postTestscore, s = df.age) 
# 图上点的size用x来表示，参数设置为s = x，而且所有参数不需要带引号，因为是数字
plt.xlabel('preTestscore')
plt.ylabel('postTestscore')
plt.title('preTestscore x postTestscore')
plt.show()

### Step 4. Create a Scatterplot of preTestScore and postTestScore
### This time the size should be 4.5 times the postTestScore and the color 
### determined by sex
plt.scatter(df.preTestscore, df.postTestscore, c = df.female, 
            s = df.preTestscore * 4.5)
plt.xlabel('preTestscore')
plt.ylabel('postTestscore')
plt.title('preTestscore x postTestscore')
plt.show()

core






### tips
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:40:29 2020

@author: Gan
"""

### Step 1. Import the necessary libraries:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv'

### Step 3. Assign it to a variable called tips
tips = pd.read_csv(url, engine = 'python')

### Step 4. Delete the Unnamed 0 column
del tips['Unamed: 0']

### Step 5. Plot the total_bill column histogram
his = tips['total_bill'].value_counts()
his.plot(kind = 'bar')

ttbill = sns.distplot(tips.total_bill)
# seaborn的displot()集合了matplotlib的hist()，直接绘制直方图
ttbill.set(xlabel = 'Value', ylabel = 'Frequency', title = 'Total Bill')
# 设置坐标轴和标题
sns.despine()
# take out the right and upper borders

### Step 6. Create a scatter plot presenting the relationship between 
### total_bill and tip
sns.jointplot(x = 'total_bill', y ='tip', data = tips)
# sns.jointplot画的是两个变量之间的相关性，坐标是R^2的相关系数，数据来源在最后

### Step 7.  Create one image with the relationship of total_bill, tip and size
#### Hint: It is just one function
# pairwise relationship即多个变量中两两变量之间的相关系
sns.pairplot(tips[['total_bill', 'tip', 'size']])
sns.pairplot(tips)

### Step 8. Present the relationship between days and total_bill value
sns.jointplot( x = 'days', y = 'total_bill', data = tips)

### Step 9. Create a scatter plot with the day as the y-axis and tip as the
### x-axis, differ the dots by sex
plt.scatter(tips.tip, tips.day, c = tips.female) 
sns.stripplot(x = 'tip', y = 'day', hue = 'sex', data = tips, jitter = True)
# sns中的分布散点图

### Step 10.  Create a box plot presenting the total_bill per day 
### differetiation the time (Dinner or Lunch)
sns.boxplot(x = 'day', y = 'total_bill', hue = 'time', data = tips)
# 箱形图（Box-plot）又称为盒须图、盒式图或箱线图，是一种用作显示一组数据分散情况资
# 料的统计图。它能显示出一组数据的最大值、最小值、中位数及上下四分位数

### Step 11. Create two histograms of the tip value based for Dinner and Lunch. 
### They must be side by side
sns.set(style = 'ticks')
g = sns.FacetGrid(tips, col = 'time')
g.map(plt.hist, 'tip')

### Step 12. Create two scatterplots graphs, one for Male and another for 
### Female, presenting the total_bill value and tip relationship, differing by 
### smoker or no smoker
g = sns.FacetGrid(tips, col = 'sex', hue = 'smoker')
# hue相当于多一个维度，在x和y轴下来区分样本点，类似于标签







### titanic
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:38:20 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Visualization/Titanic_Desaster/train.csv)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Visualization/Titanic_Desaster/train.csv'

### Step 3. Assign it to a variable titanic
titanic = pd.read_csv(url, engine = 'python')

### Step 4. Set PassengerId as the index
titanic.set_index('PasengerID')

### Step 5. Create a pie chart presenting the male/female proportion
proportion = titanic.groupby('sex').sum()
plt.pie(proportion)
# pyplot.pie(x, explode=None, labels=None……）
             
# sum the instances of males and females
males = (titanic['Sex'] == 'male').sum()
females = (titanic['Sex'] == 'female').sum()
# put them into a list called proportions
proportions = [males, females]
# Create a pie chart
plt.pie(proportions, labels = ['Males', 'Females'], shadow = False,
        colors = ['blue','red'], explode = (0.15 , 0), startangle = 90 )
# View the plot drop above
plt.axis('equal')
plt.title('Sex Proportion')
plt.tight_layout()
plt.show

### Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender
plt.scatter(titanic.fare, titanic.Age, c = titanic.gender)

lm = sns.lmplot(x = 'Age', y = 'Fare', data = titanic, hue = 'Sex', fit_reg=False)
lm.set(title = 'Fare x Age')
axes = lm.axes
axes[0,0].set_ylim(-5,)
axes[0,0].set_xlim(-5,85)

### Step 7. How many people survived?
titanic.survive.sum()

### Step 8. Create a histogram with the Fare payed
his = titanic.fare.sort_values(ascending = False)
# create bins interval using numpy
binsVal = np.arange(0,600,10)

plt.hist(his, bins = binsVal) 
# bins是表示颜色范围
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()