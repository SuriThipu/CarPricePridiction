import Header as m

m.df['brand'] = m.df.CarName.str.split(' ').str.get(0).str.upper()


m.df_comp_avg_price = m.df[['brand','price']].groupby("brand", as_index = False).mean().rename(columns={'price':'brand_avg_price'})
m.plt1 = m.df_comp_avg_price.plot(x = 'brand', kind='bar',legend = False, sort_columns = True, figsize = (15,3))
m.plt1.set_xlabel("Brand")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 90)
m.plt.show()
