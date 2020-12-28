import Header as m


#checking duplicates
sum(m.df.duplicated(subset = 'car_ID')) == 0
# No duplicate values

# Checking Null values
m.df.isnull().sum()*100/m.df.shape[0]
# There are no NULL values in the dataset, hence it is clean.

m.df_body_avg_price = m.df[['carbody','price']].groupby("carbody", as_index = False).mean().rename(columns={'price':'carbody_avg_price'})
m.plt1 = m.df_body_avg_price.plot(x = 'carbody', kind='bar',legend = False, sort_columns = True)
m.plt1.set_xlabel("Car Body")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 0)
m.plt.show() 