import Header as m

m.df['brand'] = m.df.CarName.str.split(' ').str.get(0).str.upper()


m.df_comp_avg_price = m.df[['brand','price']].groupby("brand", as_index = False).mean().rename(columns={'price':'brand_avg_price'})

m.df = m.df.merge(m.df_comp_avg_price, on = 'brand')

m.df['brand_cat'] = m.df['brand_avg_price'].apply(lambda x : "Budget" if x < 10000 
                                                     else ("Mid_Range" if 10000 <= x < 20000
                                                           else "Luxury"))



m.plt1 = m.sns.scatterplot(x = 'horsepower', y = 'price', hue = 'brand_cat', data = m.df)
m.plt1.set_xlabel('Horsepower')
m.plt1.set_ylabel('Price of Car (Dollars)')
m.plt.show()