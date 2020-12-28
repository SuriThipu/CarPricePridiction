#import Header as m

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.pyplot import xticks

df = pd.DataFrame(pd.read_csv("CarPrice_Assignment.csv"))

df.head()
#df.info()

#checking duplicates
sum(df.duplicated(subset = 'car_ID')) == 0
# No duplicate values

# Checking Null values
df.isnull().sum()*100/df.shape[0]
# There are no NULL values in the dataset, hence it is clean.

sns.distplot(df['price'])

plt.show()