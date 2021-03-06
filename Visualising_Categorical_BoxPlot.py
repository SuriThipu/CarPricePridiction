import Header as m



m.df['brand'] = m.df.CarName.str.split(' ').str.get(0).str.upper()

m.df_comp_avg_price = m.df[['brand','price']].groupby("brand", as_index = False).mean().rename(columns={'price':'brand_avg_price'})

m.df = m.df.merge(m.df_comp_avg_price, on = 'brand')

m.df['brand_category'] = m.df['brand_avg_price'].apply(lambda x : "Budget" if x < 10000 
                                                     else ("Mid_Range" if 10000 <= x < 20000
                                                           else "Luxury"))



m.df['mileage'] = m.df['citympg']*0.55 + m.df['highwaympg']*0.45


auto = m.df[['fueltype', 'aspiration', 'carbody', 'drivewheel', 'wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginetype',
       'cylindernumber', 'enginesize',  'boreratio', 'horsepower', 'price', 'brand_category', 'mileage']]


m.plt.figure(figsize=(10, 20))
m.plt.subplot(4,2,1)
m.sns.boxplot(x = 'fueltype', y = 'price', data = auto)
m.plt.subplot(4,2,2)
m.sns.boxplot(x = 'aspiration', y = 'price', data = auto)
m.plt.subplot(4,2,3)
m.sns.boxplot(x = 'carbody', y = 'price', data = auto)
m.plt.subplot(4,2,4)
m.sns.boxplot(x = 'drivewheel', y = 'price', data = auto)
m.plt.subplot(4,2,5)
m.sns.boxplot(x = 'enginetype', y = 'price', data = auto)
m.plt.subplot(4,2,6)
m.sns.boxplot(x = 'brand_category', y = 'price', data = auto)
m.plt.subplot(4,2,7)
m.sns.boxplot(x = 'cylindernumber', y = 'price', data = auto)
m.plt.tight_layout()
m.plt.show()
