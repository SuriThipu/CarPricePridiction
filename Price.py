import Header as m


#checking duplicates
sum(m.df.duplicated(subset = 'car_ID')) == 0
# No duplicate values

# Checking Null values
m.df.isnull().sum()*100/m.df.shape[0]
# There are no NULL values in the dataset, hence it is clean.

m.sns.distplot(m.df['price'])

m.plt.show()