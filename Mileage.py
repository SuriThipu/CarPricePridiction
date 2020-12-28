import Header as m

# A single variable mileage can be calculated taking the weighted average of 55% city and 45% highways.
m.df['mileage'] = m.df['citympg']*0.55 + m.df['highwaympg']*0.45

m.plt1 = m.sns.scatterplot(x = 'mileage', y = 'price', data = m.df)
m.plt1.set_xlabel('Mileage')
m.plt1.set_ylabel('Price of Car (Dollars)')
m.plt.show()