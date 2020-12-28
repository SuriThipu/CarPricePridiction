import Header as m

# A single variable mileage can be calculated taking the weighted average of 55% city and 45% highways.
m.df['mileage'] = m.df['citympg']*0.55 + m.df['highwaympg']*0.45

m.df['brand'] = m.df.CarName.str.split(' ').str.get(0).str.upper()

df_comp_avg_price = m.df[['brand','price']].groupby("brand", as_index = False).mean().rename(columns={'price':'brand_avg_price'})

m.df = m.df.merge(df_comp_avg_price, on = 'brand')

m.df['Brand_cat'] = m.df['brand_avg_price'].apply(lambda x : "Budget" if x < 10000 
                                                     else ("Mid_Range" if 10000 <= x < 20000
                                                           else "Luxury"))



m.plt1 = m.sns.scatterplot(x = 'mileage', y = 'price', hue = 'Brand_cat', data = m.df)
m.plt1.set_xlabel('Mileage')
m.plt1.set_ylabel('Price of Car (Dollars)')
m.plt.show()
