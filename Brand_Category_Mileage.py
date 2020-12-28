import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.pyplot import xticks

df = pd.DataFrame(pd.read_csv("CarPrice_Assignment.csv"))

# A single variable mileage can be calculated taking the weighted average of 55% city and 45% highways.
df['mileage'] = df['citympg']*0.55 + df['highwaympg']*0.45

df['brand'] = df.CarName.str.split(' ').str.get(0).str.upper()

df_comp_avg_price = df[['brand','price']].groupby("brand", as_index = False).mean().rename(columns={'price':'brand_avg_price'})

df = df.merge(df_comp_avg_price, on = 'brand')

df['Brand_cat'] = df['brand_avg_price'].apply(lambda x : "Budget" if x < 10000 
                                                     else ("Mid_Range" if 10000 <= x < 20000
                                                           else "Luxury"))



plt1 = sns.scatterplot(x = 'mileage', y = 'price', hue = 'Brand_cat', data = df)
plt1.set_xlabel('Mileage')
plt1.set_ylabel('Price of Car (Dollars)')
plt.show()
