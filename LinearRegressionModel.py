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

m.plt.figure(figsize=(15, 15))
m.sns.pairplot(auto)
m.plt.show()
