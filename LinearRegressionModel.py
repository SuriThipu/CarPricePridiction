import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.pyplot import xticks

df = pd.DataFrame(pd.read_csv("CarPrice_Assignment.csv"))

df['brand'] = df.CarName.str.split(' ').str.get(0).str.upper()

df_comp_avg_price = df[['brand','price']].groupby("brand", as_index = False).mean().rename(columns={'price':'brand_avg_price'})

df = df.merge(df_comp_avg_price, on = 'brand')

df['brand_category'] = df['brand_avg_price'].apply(lambda x : "Budget" if x < 10000 
                                                     else ("Mid_Range" if 10000 <= x < 20000
                                                           else "Luxury"))



df['mileage'] = df['citympg']*0.55 + df['highwaympg']*0.45

auto = df[['fueltype', 'aspiration', 'carbody', 'drivewheel', 'wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginetype',
       'cylindernumber', 'enginesize',  'boreratio', 'horsepower', 'price', 'brand_category', 'mileage']]

plt.figure(figsize=(15, 15))
sns.pairplot(auto)
plt.show()