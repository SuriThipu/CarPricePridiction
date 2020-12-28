import Header as m


m.plt1 =  m.sns.scatterplot(x = 'horsepower', y = 'price', hue = 'fueltype', data = m.df)
m.plt1.set_xlabel('Horsepower')
m.plt1.set_ylabel('Price of Car (Dollars)')
m.plt.show()