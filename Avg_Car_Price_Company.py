import warnings
warnings.filterwarnings('ignore')
import Header as m

m.df.head()


#checking duplicates
sum(m.df.duplicated(subset = 'car_ID')) == 0
# No duplicate values

# Checking Null values
m.df.isnull().sum()*100/m.df.shape[0]
# There are no NULL values in the dataset, hence it is clean.


m.df.CarName.values[0:10]

# It is observed that Car Name consists of two parts 'car company' + ' ' + 'Car Model'
# Let's split out car company to a new column.
m.df['brand'] = m.df.CarName.str.split(' ').str.get(0).str.upper()


len(set(m.df.brand.values))


# Let's see average car price of each company.

m.df_comp_avg_price = m.df[['brand','price']].groupby("brand", as_index = False).mean().rename(columns={'price':'brand_avg_price'})
m.plt1 = m.df_comp_avg_price.plot(x = 'brand', kind='bar',legend = False, sort_columns = True, figsize = (15,3))
m.plt1.set_xlabel("Brand")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 90)
m.plt.show()