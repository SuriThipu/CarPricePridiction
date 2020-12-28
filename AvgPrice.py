import Header as m


#checking duplicates
sum(m.df.duplicated(subset = 'car_ID')) == 0
# No duplicate values

# Checking Null values
m.df.isnull().sum()*100/m.df.shape[0]
# There are no NULL values in the dataset, hence it is clean.


# Let's see average price of cars in each symbol category.
m.plt1 = m.df[['symboling','price']].groupby("symboling").mean().plot(kind='bar',legend = False,)
m.plt1.set_xlabel("Symbol")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 0)
m.plt.show()