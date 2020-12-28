import Header as m


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


# Let's see companies and their no of models.
fig, ax = m.plt.subplots(figsize = (15,5))
m.plt1 = m.sns.countplot(m.df['brand'], order=m.pd.value_counts(m.df['brand']).index,)
m.plt1.set(xlabel = 'Brand', ylabel= 'Count of Cars')
m.xticks(rotation = 90)
m.plt.show()
m.plt.tight_layout()

